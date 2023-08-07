import os
from pathlib import Path
import re

ATTACHMENT_FOLDER = "attachments"


class Organizer:
    def __init__(self, root: Path):
        self.root = root
        self.mappings = {}

    def organize(self):
        for child in self.root.rglob("*"):
            if child.is_dir() or child.suffix == ".md":
                continue

            self.organize_attachment(child)

        for child in self.root.rglob("*.md"):
            self.fix_links(child)

        for child in self.root.rglob("*"):
            if child.is_dir() and not any(child.iterdir()):
                os.rmdir(child)

    def organize_attachment(self, file: Path):
        new_path = path_for_attachment(file)

        self.save_mapping(file, new_path)

        os.makedirs(new_path.parent, exist_ok=True)
        file.rename(new_path)

    def fix_links(self, file: Path):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        link_pattern = re.compile(r"\[\[(.*)\]\]")
        content = link_pattern.sub(self.fix_link(file), content)

        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

    def save_mapping(self, old: Path, new: Path):
        old = str(old.relative_to(self.root))
        new = str(new.relative_to(self.root))

        self.mappings[old] = new

    def fix_link(self, file: Path):
        def fix_link(match) -> str:
            link = match.group(1)
            link = file.parent / link
            link = Path(os.path.normpath(link))
            link = link.relative_to(self.root)
            link = str(link)

            if link in self.mappings.keys():
                link = self.mappings[link]
                link = link.replace("\\", "/")
                return f"[[{link}]]"

            return match.group(0)

        return fix_link


def path_for_attachment(file: Path) -> Path:
    parent, stem, suffix = file.parent, file.stem, file.suffix

    stem = parent.stem
    parent = parent.parent / "attachments"

    raw_name = (parent / stem).with_suffix(suffix)

    index = 1
    new_name = raw_name.with_stem(f"{stem} {index}")

    while new_name.exists():
        index += 1
        new_name = raw_name.with_stem(f"{stem} {index}")

    return new_name
