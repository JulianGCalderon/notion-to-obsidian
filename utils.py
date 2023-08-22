from pathlib import PurePath
import re


def remove_uuid(file: PurePath) -> PurePath:
    file = PurePath(file)

    parent, stem, suffix = file.parent, file.stem, file.suffix

    clean = PurePath()

    for component in parent.parts:
        component = try_remove_uuid(component)

        clean /= component

    if suffix == ".md":
        stem = try_remove_uuid(file.stem)

    clean /= stem

    return clean.with_suffix(file.suffix)


def try_remove_uuid(component: str) -> str:
    split = component.split()
    code = split[-1]
    if len(code) == 32:
        component = " ".join(split[:-1])

    return component


def fix_structure_content(content):
    aside_pattern = re.compile(
        r"( *)<aside>\s*(?:<img .*?\/>)?[^\s]? ([\s\S]*?)\s*<\/aside>"
    )

    def sub_aside(match) -> str:
        indent, content = match.groups()
        output = f"{indent}> [!note]\n"
        for line in content.splitlines():
            output += f"{indent}> {line}\n"

        return output

    content = aside_pattern.sub(sub_aside, content)

    extra_asterisk = re.compile(r"\*{3}\**")
    content = extra_asterisk.sub(r"***", content)

    leading_header = re.compile(r"\A# .*\n*")
    content = leading_header.sub(r"", content)

    return content


def fix_math_content(content):
    real_pattern = re.compile(r"\\R(?![a-zA-Z])")
    content = real_pattern.sub(r"\\mathbb{R}", content)

    lang_pattern = re.compile(r"\\lang(?![a-zA-Z])")
    content = lang_pattern.sub(r"\\langle", content)

    rang_pattern = re.compile(r"\\rang(?![a-zA-Z])")
    content = rang_pattern.sub(r"\\rangle", content)

    dag_pattern = re.compile(r"\\dag(?![a-zA-Z])")
    content = dag_pattern.sub(r"\\dagger", content)

    footnotesize_pattern = re.compile(r"\\footnotesize(?![a-zA-Z])")
    content = footnotesize_pattern.sub(r"\\small ", content)

    empty_pattern = re.compile(r"\\empty(?![a-zA-Z])")
    content = empty_pattern.sub(r"\\emptyset", content)

    natural_pattern = re.compile(r"\\N(?![a-zA-Z])")
    content = natural_pattern.sub(r"\\mathbb{N}", content)

    oiint_pattern = re.compile(r"\\oiint\s*\\limits_")
    content = oiint_pattern.sub(r"{\\subset\\!\\supset} \\llap{\\iint}_", content)

    bare_oiint_pattern = re.compile(r"\\oiint")
    content = bare_oiint_pattern.sub(r"{\\subset\\!\\supset} \\llap{\\iint}", content)

    infin_pattern = re.compile(r"\\infin(?![a-zA-Z])")
    content = infin_pattern.sub(r"\\infty", content)

    color_pattern = re.compile(r"\\(red|green|blue|gray)(?![a-zA-Z])")
    content = color_pattern.sub(r"\\color{\1}", content)

    integer_pattern = re.compile(r"\\Z(?![a-zA-Z])")
    content = integer_pattern.sub(r"\\mathbb{Z}", content)

    complex_pattern = re.compile(r"\\Complex(?![a-zA-Z])")
    content = complex_pattern.sub(r"\\mathbb{C}", content)

    epsilon_pattern = re.compile(r"\\Epsilon(?![a-zA-Z])")
    content = epsilon_pattern.sub(r"E", content)

    mathellipsis_pattern = re.compile(r"\\mathellipsis(?![a-zA-Z])")
    content = mathellipsis_pattern.sub(r"\\dots", content)

    tau_pattern = re.compile(r"\\Tau(?![a-zA-Z])")
    content = tau_pattern.sub(r" T", content)

    tg_pattern = re.compile(r"\\tg(?![a-zA-Z])")
    content = tg_pattern.sub(r"\\tan", content)

    chi_pattern = re.compile(r"\\Chi(?![a-zA-Z])")
    content = chi_pattern.sub(r"\\chi", content)

    tag_tex_pattern = re.compile(r"\\tag{\\text{(.*)}}")
    content = tag_tex_pattern.sub(r"\\tag{\1}", content)

    bold_pattern = re.compile(r"\\bold(?![a-zA-Z])")
    content = bold_pattern.sub(r"\\mathbf", content)

    return content
