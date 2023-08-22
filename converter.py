import os
import re
import shutil

from pathlib import Path, PurePath
from urllib.parse import unquote
import zipfile

from utils import fix_math_content, fix_structure_content, remove_uuid

ATTACHMENT_FOLDER = "Attachments"


class Converter:
    def __init__(self, src_path: Path, dest_path: Path, mathjax: bool):
        self.src_path = src_path
        self.dest_path = dest_path
        self.mathjax = mathjax
        self.mappings = {}

    def convert(self):
        self.clean_folder(self.dest_path)
        self.extract_folder(self.src_path)
        self.fix_links(self.dest_path)
        self.format(self.dest_path)

    def clean_folder(self, folder: Path):
        if not folder.exists():
            return
        for child in folder.iterdir():
            if child.name == ".obsidian":
                continue
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

    def fix_links(self, vault: Path):
        for child in vault.rglob("*.md"):
            self.fix_links_in_file(child)

    def fix_links_in_file(self, file: Path):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        URL_PATTERN = re.compile(r"\[(.*)\]\((.*)\)")
        content = URL_PATTERN.sub(self.fix_link(self.relative_to_dest(file)), content)

        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

    def fix_link(self, file: Path):
        def _(match: re.Match) -> str:
            title, link = match.groups()

            HTTP_PATTERN = re.compile(r"^https?://")
            if HTTP_PATTERN.match(link):
                return match.group(0)

            link = link.lstrip("<").rstrip(">")
            link = unquote(link)
            link = remove_uuid(link)
            link = file.parent / link
            link = os.path.normpath(link)

            if self.mappings.get(link):
                link = self.mappings[link]

            if not Path(self.dest_path / link).exists():
                return match.group(0)

            link = link.replace("\\", "/")

            if title == link or title is None:
                return f"[[{link}]]"
            else:
                return f"[[{link}|{title}]]"

        return _

    def format(self, vault: Path):
        for child in vault.rglob("*.md"):
            self.fix_markdown_in_file(child)

    def fix_markdown_in_file(self, file: Path):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        if self.mathjax:
            content = fix_math_content(content)

        content = fix_structure_content(content)

        with open(file, "w", encoding="utf-8") as f:
            f.write(content)


def path_for_attachment(file: Path) -> Path:
    main_path = file.parent.parent / ATTACHMENT_FOLDER / file.parent.stem
    main_path = main_path.with_suffix(file.suffix)

    index = 1
    possible_path = main_path.with_stem(f"{main_path.stem} {index}")

    while possible_path.exists():
        index += 1
        possible_path = main_path.with_stem(f"{main_path.stem} {index}")

    return possible_path
