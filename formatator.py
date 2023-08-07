import re


def format_md_content(content: str) -> str:
    img_pattern = re.compile(r"<img .*\/>")
    content = img_pattern.sub(r"", content)

    aside_pattern = re.compile(r"<aside>\n*(.*?)\n*</aside>", re.DOTALL)
    content = aside_pattern.sub(r" > [!note]\n > \1", content)

    extra_asterisk = re.compile(r"\*{3}\**")
    content = extra_asterisk.sub(r"***", content)

    leading_header = re.compile(r"\A# .*\n*")
    content = leading_header.sub(r"", content)

    scale_down_header = re.compile(r"^(#+) ", re.MULTILINE)
    content = scale_down_header.sub(r"#\1 ", content)

    extra_newline = re.compile(r"\n\n\n*")
    content = extra_newline.sub(r"\n\n", content)

    extra_whitespace = re.compile(r"(\S)  +")
    content = extra_whitespace.sub(r"\1 ", content)

    return content
