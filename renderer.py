import os
from pathlib import PurePath
import re
from urllib.parse import unquote
from mistune.renderers.markdown import MarkdownRenderer

from utils import remove_uuid

URL_PATTERN = re.compile(r"https?:\/\/")


class MyRenderer(MarkdownRenderer):
    def __init__(self, file, mappings):
        self.file = file
        self.mapping = mappings

        super().__init__()

    def link(self, token, state):
        title = self.render_children(token, state)
        attrs = token["attrs"]
        url = attrs["url"]

        if URL_PATTERN.match(url):
            title = PurePath(url).name
            return f"[{title}]({url})"

        url = unquote(url)
        url = remove_uuid(url)
        url = self.file.parent / url
        url = os.path.normpath(url)

        if self.mapping.get(url):
            url = self.mapping[url]

        url = url.replace("\\", "/")

        return f"[[{url}|{title}]]"

    def block_math(self, text, state):
        equation = text["raw"]

        equation = self.format_math(equation)

        return f"$$\n{equation}\n$$\n"

    def inline_math(self, text, state):
        equation = text["raw"]

        equation = self.format_math(equation)

        return f"${equation}$"

    def format_math(self, equation):
        real_pattern = re.compile(r"\\R(?![a-zA-Z])")
        equation = real_pattern.sub(r"\\mathbb{R}", equation)

        lang_pattern = re.compile(r"\\lang(?![a-zA-Z])")
        equation = lang_pattern.sub(r"\\langle", equation)

        rang_pattern = re.compile(r"\\rang(?![a-zA-Z])")
        equation = rang_pattern.sub(r"\\rangle", equation)

        dag_pattern = re.compile(r"\\dag(?![a-zA-Z])")
        equation = dag_pattern.sub(r"\\dagger", equation)

        footnotesize_pattern = re.compile(r"\\footnotesize(?![a-zA-Z])")
        equation = footnotesize_pattern.sub(r"\\small ", equation)

        empty_pattern = re.compile(r"\\empty(?![a-zA-Z])")
        equation = empty_pattern.sub(r"\\emptyset", equation)

        natural_pattern = re.compile(r"\\N(?![a-zA-Z])")
        equation = natural_pattern.sub(r"\\mathbb{N}", equation)

        oiint_pattern = re.compile(r"\\oiint\s*\\limits_")
        equation = oiint_pattern.sub(r"{\\subset\\!\\supset} \\llap{\\iint}_", equation)

        bare_oiint_pattern = re.compile(r"\\oiint")
        equation = bare_oiint_pattern.sub(
            r"{\\subset\\!\\supset} \\llap{\\iint}", equation
        )

        infin_pattern = re.compile(r"\\infin(?![a-zA-Z])")
        equation = infin_pattern.sub(r"\\infty", equation)

        color_pattern = re.compile(r"\\(red|green|blue|gray)(?![a-zA-Z])")
        equation = color_pattern.sub(r"\\color{\1}", equation)

        integer_pattern = re.compile(r"\\Z(?![a-zA-Z])")
        equation = integer_pattern.sub(r"\\mathbb{Z}", equation)

        complex_pattern = re.compile(r"\\Complex(?![a-zA-Z])")
        equation = complex_pattern.sub(r"\\mathbb{C}", equation)

        epsilon_pattern = re.compile(r"\\Epsilon(?![a-zA-Z])")
        equation = epsilon_pattern.sub(r"E", equation)

        mathellipsis_pattern = re.compile(r"\\mathellipsis(?![a-zA-Z])")
        equation = mathellipsis_pattern.sub(r"\\dots", equation)

        tau_pattern = re.compile(r"\\Tau(?![a-zA-Z])")
        equation = tau_pattern.sub(r" T", equation)

        tg_pattern = re.compile(r"\\tg(?![a-zA-Z])")
        equation = tg_pattern.sub(r"\\tan", equation)

        chi_pattern = re.compile(r"\\Chi(?![a-zA-Z])")
        equation = chi_pattern.sub(r"\\chi", equation)

        tag_tex_pattern = re.compile(r"\\tag{\\text{(.*)}}")
        equation = tag_tex_pattern.sub(r"\\tag{\1}", equation)

        bold_pattern = re.compile(r"\\bold(?![a-zA-Z])")
        equation = bold_pattern.sub(r"\\mathbf", equation)

        return equation
