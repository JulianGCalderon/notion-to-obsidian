import os
from pathlib import Path, PurePath
import re
import zipfile
import shutil
from urllib.parse import unquote
import mistune
from mistune.renderers.markdown import MarkdownRenderer

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

    def extract(self) -> Path:
        shutil.rmtree(self.vault_path, ignore_errors=True)

        self.extract_folder(self.export_path)
        self.format_folder(self.vault_path)

        return self.vault_path

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

        self.mappings[relative_old_path] = relative_new_path

        self.extract_file_to(file, full_new_path)

    def extract_md(self, file: zipfile.Path):
        relative_path = remove_uuid(self.relative_to_export(file))
        full_path = self.vault_path / relative_path

        self.extract_file_to(file, full_path)

    def extract_file_to(self, file: zipfile.Path, destination: Path) -> Path:
        with file.open("rb") as f:
            content = f.read()

        os.makedirs(destination.parent, exist_ok=True)
        with open(destination, "wb") as f:
            f.write(content)

    def relative_to_export(self, file) -> PurePath:
        return PurePath(str(file)).relative_to(str(self.export_path))

    def relative_to_vault(self, file) -> PurePath:
        return PurePath(str(file)).relative_to(str(self.vault_path))

    def format_folder(self, folder: Path):
        for child in folder.rglob("*.md"):
            self.format_md(child)

    def format_md(self, file: Path):
        with file.open("r", encoding="utf-8") as f:
            content = f.read()

        relative_path = self.relative_to_vault(file)
        markdown = mistune.create_markdown(
            renderer=MarkdownFormatter(relative_path, self.mappings), plugins=["math"]
        )
        content = markdown(content)

        with file.open("w", encoding="utf-8") as f:
            f.write(content)


class MarkdownFormatter(MarkdownRenderer):
    def __init__(self, file, mappings):
        self.file = file
        self.mapping = mappings

        super().__init__()

    def link(self, token, state):
        title = self.render_children(token, state)
        attrs = token["attrs"]
        url = attrs["url"]

        if URL_PATTERN.match(url):
            return super().link(token, state)

        url = unquote(url)
        url = remove_uuid(url)
        url = self.file.parent / url
        url = os.path.normpath(url)
        url = Path(url)

        if self.mapping.get(url):
            url = self.mapping[url]

        url = str(url).replace("\\", "/")

        return f"[[{url}|{title}]]"

    def block_math(self, text, state):
        raw = text["raw"]

        raw = self.format_math(raw)

        return f"$$\n{raw}\n$$\n"

    def inline_math(self, text, state):
        raw = text["raw"]

        raw = self.format_math(raw)

        return f"${raw}$"

    def format_math(self, raw):
        real_pattern = re.compile(r"\\R(?![a-zA-Z])")
        raw = real_pattern.sub(r"\\mathbb{R}", raw)

        lang_pattern = re.compile(r"\\lang(?![a-zA-Z])")
        raw = lang_pattern.sub(r"\\langle", raw)

        rang_pattern = re.compile(r"\\rang(?![a-zA-Z])")
        raw = rang_pattern.sub(r"\\rangle", raw)

        dag_pattern = re.compile(r"\\dag(?![a-zA-Z])")
        raw = dag_pattern.sub(r"\\dagger", raw)

        footnotesize_pattern = re.compile(r"\\footnotesize(?![a-zA-Z])")
        raw = footnotesize_pattern.sub(r"\\small ", raw)

        empty_pattern = re.compile(r"\\empty(?![a-zA-Z])")
        raw = empty_pattern.sub(r"\\emptyset", raw)

        natural_pattern = re.compile(r"\\N(?![a-zA-Z])")
        raw = natural_pattern.sub(r"\\mathbb{N}", raw)

        oiint_pattern = re.compile(r"\\oiint\s*\\limits_")
        raw = oiint_pattern.sub(r"{\\subset\\!\\supset} \\llap{\\iint}_", raw)

        bare_oiint_pattern = re.compile(r"\\oiint")
        raw = bare_oiint_pattern.sub(r"{\\subset\\!\\supset} \\llap{\\iint}", raw)

        infin_pattern = re.compile(r"\\infin(?![a-zA-Z])")
        raw = infin_pattern.sub(r"\\infty", raw)

        color_pattern = re.compile(r"\\(red|green|blue|gray)(?![a-zA-Z])")
        raw = color_pattern.sub(r"\\color{\1}", raw)

        integer_pattern = re.compile(r"\\Z(?![a-zA-Z])")
        raw = integer_pattern.sub(r"\\mathbb{Z}", raw)

        complex_pattern = re.compile(r"\\Complex(?![a-zA-Z])")
        raw = complex_pattern.sub(r"\\mathbb{C}", raw)

        epsilon_pattern = re.compile(r"\\Epsilon(?![a-zA-Z])")
        raw = epsilon_pattern.sub(r"E", raw)

        mathellipsis_pattern = re.compile(r"\\mathellipsis(?![a-zA-Z])")
        raw = mathellipsis_pattern.sub(r"\\dots", raw)

        tau_pattern = re.compile(r"\\Tau(?![a-zA-Z])")
        raw = tau_pattern.sub(r" T", raw)

        tg_pattern = re.compile(r"\\tg(?![a-zA-Z])")
        raw = tg_pattern.sub(r"\\tan", raw)

        chi_pattern = re.compile(r"\\Chi(?![a-zA-Z])")
        raw = chi_pattern.sub(r"\\chi", raw)

        tag_tex_pattern = re.compile(r"\\tag{\\text{(.*)}}")
        raw = tag_tex_pattern.sub(r"\\tag{\1}", raw)

        bold_pattern = re.compile(r"\\bold(?![a-zA-Z])")
        raw = bold_pattern.sub(r"\\mathbf", raw)

        return raw


def path_for_attachment(file: Path) -> Path:
    main_path = file.parent.parent / ATTACHMENT_FOLDER / file.parent.stem
    main_path = main_path.with_suffix(file.suffix)

    index = 1
    possible_path = main_path.with_stem(f"{main_path.stem} {index}")

    while possible_path.exists():
        index += 1
        possible_path = main_path.with_stem(f"{main_path.stem} {index}")

    return possible_path
