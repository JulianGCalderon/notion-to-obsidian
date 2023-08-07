import os
from pathlib import Path, PurePath
import re
import zipfile
import shutil
from urllib.parse import unquote

from utils import remove_uuid, to_pure_path

EXTRACT_FOLDER = "extracted"


class Extractor:
    def __init__(self, export_path: zipfile.Path):
        self.export_path = export_path
        self.extract_path = export_path.parent / EXTRACT_FOLDER

    def relative_path(self, file) -> PurePath:
        return to_pure_path(file).relative_to(to_pure_path(self.export_path))

    def relative_path_to_extract(self, file) -> PurePath:
        return to_pure_path(file).relative_to(to_pure_path(self.extract_path))

    def extract(self) -> Path:
        shutil.rmtree(self.extract_path, ignore_errors=True)

        self.extract_folder(self.export_path)

        return self.extract_path

    def extract_folder(self, export: zipfile.Path) -> Path:
        for child in export.iterdir():
            if child.is_dir():
                self.extract_folder(child)
            else:
                self.extract_file(child)

    def extract_file(self, file: zipfile.Path) -> Path:
        relative_path = self.relative_path(file)
        destination = remove_uuid(relative_path)
        full_path = self.extract_path / destination

        with file.open("rb") as f:
            content = f.read()

        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "wb") as f:
            f.write(content)

        if file.suffix == ".md":
            self.fix_links(full_path)

    def fix_links(self, file: Path):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        relative_to_vault = self.relative_path_to_extract(file)

        link_pattern = re.compile(r"\[(.*)\]\((.*)\)")
        content = link_pattern.sub(fix_link_for_root(relative_to_vault), content)

        with open(file, "w", encoding="utf-8") as f:
            f.write(content)


def fix_link_for_root(file: Path):
    def fix_link(match):
        title, link = match.groups()

        if link.startswith("https://") or link.startswith("http://"):
            return match.group(0)

        link = unquote(link)
        link = remove_uuid(link)
        link = str(link).replace("\\", "/")

        return f"![[{link}]]"

    return fix_link
