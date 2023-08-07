import os
from pathlib import Path, PurePath
import re
import zipfile
import shutil
from urllib.parse import unquote

from utils import remove_uuid


VAULT_FOLDER = "vault"


class Extractor:
    def __init__(self, export_path: zipfile.Path):
        self.export_path = export_path
        self.vault_path = Path(str(export_path)).parent / VAULT_FOLDER

    def relative_to_export(self, file) -> PurePath:
        return PurePath(str(file)).relative_to(str(self.export_path))

    def relative_to_vault(self, file) -> PurePath:
        return PurePath(str(file)).relative_to(self.vault_path)

    def extract(self) -> Path:
        shutil.rmtree(self.vault_path, ignore_errors=True)

        self.extract_folder(self.export_path)

        return self.extract_path

    def extract_folder(self, export: zipfile.Path) -> Path:
        for child in export.iterdir():
            if child.is_dir():
                self.extract_folder(child)
            else:
                self.extract_file(child)

    def extract_file(self, file: zipfile.Path) -> Path:
        relative_to_export = self.relative_to_export(file)
        relative_to_vault = remove_uuid(relative_to_export)
        relative_to_cwd = self.vault_path / relative_to_vault

        os.makedirs(relative_to_cwd.parent, exist_ok=True)

        with file.open("rb") as f:
            content = f.read()

        with open(relative_to_cwd, "wb") as f:
            f.write(content)

        if file.suffix == ".md":
            self.fix_links(relative_to_cwd)

    def fix_links(self, file: Path):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        link_pattern = re.compile(r"\[(.*)\]\((.*)\)")
        content = link_pattern.sub(fix_link, content)

        with open(file, "w", encoding="utf-8") as f:
            f.write(content)


def fix_link(match):
    title, link = match.groups()

    if link.startswith("https://") or link.startswith("http://"):
        return match.group(0)

    link = unquote(link)
    link = remove_uuid(link)
    link = str(link).replace("\\", "/")

    return f"![[{link}]]"
