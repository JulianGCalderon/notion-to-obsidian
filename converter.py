import os
from pathlib import Path, PurePath
import zipfile
import shutil
import mistune
from formatator import format_md_content

from renderer import MyRenderer
from utils import remove_uuid

VAULT_FOLDER = "Vault"
ATTACHMENT_FOLDER = "Attachments"


class Converter:
    def __init__(self, src_path: Path, dest_path: Path):
        self.src_path = src_path
        self.dest_path = dest_path
        self.mappings = {}

    def convert(self):
        self.clean_folder(self.dest_path)
        self.extract_folder(self.src_path)
        self.fix_links(self.dest_path)
        self.format(self.dest_path)

    def clean_folder(self, folder: Path):
        for child in folder.iterdir():
            if child.is_dir():
                shutil.rmtree(child)

    def extract_folder(self, folder: zipfile.Path) -> Path:
        for child in folder.iterdir():
            if child.is_dir():
                self.extract_folder(child)
            else:
                self.extract_file(child)

    def extract_file(self, file: zipfile.Path) -> Path:
        if file.suffix == ".md":
            self.extract_md(file)
        else:
            self.extract_attachment(file)

    def extract_md(self, src: zipfile.Path):
        relative_dest = remove_uuid(self.relative_to_src(src))
        absolute_dest = self.dest_path / relative_dest

        self.extract_to(src, absolute_dest)

    def extract_attachment(self, file: zipfile.Path):
        relative_old = remove_uuid(self.relative_to_src(file))
        absolute_old = self.dest_path / relative_old
        absolute_new = path_for_attachment(absolute_old)
        relative_new = self.relative_to_dest(absolute_new)

        self.mappings[str(relative_old)] = str(relative_new)

        self.extract_to(file, absolute_new)

    def extract_to(self, file: zipfile.Path, destination: Path) -> Path:
        with file.open("rb") as f:
            content = f.read()

        os.makedirs(destination.parent, exist_ok=True)

        with open(destination, "wb") as f:
            f.write(content)

    def relative_to_src(self, file) -> PurePath:
        return PurePath(str(file)).relative_to(str(self.src_path))

    def relative_to_dest(self, file) -> PurePath:
        return PurePath(str(file)).relative_to(str(self.dest_path))

    def format(self, folder: Path):
        for child in folder.rglob("*.md"):
            self.format_md(child)

    def format_md(self, file: Path):
        with file.open("r", encoding="utf-8") as f:
            content = f.read()

        content = self.format_md_content(content, file)

        with file.open("w", encoding="utf-8") as f:
            f.write(content)

    def format_md_content(self, content: str, file) -> str:
        relative_path = self.relative_to_dest(file)
        markdown = mistune.create_markdown(
            renderer=MyRenderer(relative_path, self.mappings),
            plugins=["math"],
        )
        content = markdown(content)

        content = format_md_content(content)
        return content

    def fix_links(self, folder: Path):
        pass


def path_for_attachment(file: Path) -> Path:
    main_path = file.parent.parent / ATTACHMENT_FOLDER / file.parent.stem
    main_path = main_path.with_suffix(file.suffix)

    index = 1
    possible_path = main_path.with_stem(f"{main_path.stem} {index}")

    while possible_path.exists():
        index += 1
        possible_path = main_path.with_stem(f"{main_path.stem} {index}")

    return possible_path
