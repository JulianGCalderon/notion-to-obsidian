import os
from pathlib import Path, PurePath
import re
import zipfile
import shutil
from urllib.parse import unquote

from utils import remove_uuid


VAULT_FOLDER = "Vault"
ATTACHMENT_FOLDER = "Attachments"

LINK_PATTERN = re.compile(r"\[(.*?)\]\((.*?\..*)\)")
URL_PATTERN = re.compile(r"https?://.*")


class Extractor:
    def __init__(self, export_path: zipfile.Path):
        self.export_path = export_path
        self.vault_path = Path(str(export_path)).parent / VAULT_FOLDER
        self.mappings = {}

    def relative_to_export(self, file) -> PurePath:
        return PurePath(str(file)).relative_to(str(self.export_path))

    def relative_to_vault(self, file) -> PurePath:
        return PurePath(str(file)).relative_to(self.vault_path)

    def extract(self) -> Path:
        shutil.rmtree(self.vault_path, ignore_errors=True)

        self.extract_folder(self.export_path)
        self.fix_links(self.vault_path)

        self.clean_empty_folders(self.vault_path)

        return self.vault_path

    def fix_links(self, root: Path):
        for child in root.rglob("*.md"):
            with open(child, "r", encoding="utf-8") as f:
                content = f.read()

            relative_path = self.relative_to_vault(child)
            content = LINK_PATTERN.sub(self.fix_link(relative_path), content)

            with open(child, "w", encoding="utf-8") as f:
                f.write(content)

    def extract_folder(self, export: zipfile.Path) -> Path:
        for child in export.iterdir():
            if child.is_dir():
                self.extract_folder(child)
            else:
                self.extract_file(child)

    def extract_file(self, file: zipfile.Path) -> Path:
        if file.suffix == ".md":
            self.extract_md(file)
        else:
            self.extract_attachment(file)

    def extract_attachment(self, file: zipfile.Path):
        relative_old_path = remove_uuid(self.relative_to_export(file))
        full_old_path = self.vault_path / relative_old_path
        full_new_path = path_for_attachment(full_old_path)
        relative_new_path = self.relative_to_vault(full_new_path)

        self.mappings[str(relative_old_path)] = str(relative_new_path)

        with file.open("rb") as f:
            content = f.read()

        os.makedirs(full_new_path.parent, exist_ok=True)
        with open(full_new_path, "wb") as f:
            f.write(content)

    def extract_md(self, file: zipfile.Path):
        relative_path = remove_uuid(self.relative_to_export(file))
        full_path = self.vault_path / relative_path

        with file.open("r", encoding="utf-8") as f:
            content = f.read()

        os.makedirs(full_path.parent, exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    def clean_empty_folders(self, folder: Path):
        for child in folder.iterdir():
            if child.is_dir():
                self.clean_empty_folders(child)

        if not any(folder.iterdir()):
            folder.rmdir()

    def fix_link(self, relative_path: Path):
        def fix_link(match):
            title, link = match.groups()

            if URL_PATTERN.search(link):
                return match.group(0)

            link = unquote(link)
            link = remove_uuid(link)
            link = relative_path.parent / link
            link = os.path.normpath(link)

            if link in self.mappings:
                link = self.mappings[link]

            link = link.replace("\\", "/")

            if link == title:
                return f"[[{link}]]"
            else:
                return f"[[{link}|{title}]]"

        return fix_link


def path_for_attachment(file: Path) -> Path:
    main_path = file.parent.parent / ATTACHMENT_FOLDER / file.parent.stem
    main_path = main_path.with_suffix(file.suffix)

    index = 1
    possible_path = main_path.with_stem(f"{main_path.stem} {index}")

    while possible_path.exists():
        index += 1
        possible_path = main_path.with_stem(f"{main_path.stem} {index}")

    return possible_path
