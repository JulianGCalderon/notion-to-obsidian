from pathlib import Path
import regex as re

VAULT = Path("Vault")
NEW_VAULT = Path("C:\\Users\\Julian\\Vaults\\Facultad")


def find_acronyms(content):
    headding_with_acronym_pattern = re.compile(
        r"^#+ .*? ([A-Z]{2}[A-Z]*).*?", re.MULTILINE
    )
    return headding_with_acronym_pattern.findall(content)


def find_compound(content):
    compound_pattern = re.compile(r"^#+ .*?((?:[a-zA-Z]+-)+[a-zA-Z]*).*?", re.MULTILINE)
    return compound_pattern.findall(content)


def csv_print(acronyms):
    print(", ".join(acronyms))


def fix_token(tokens):
    def _(heading) -> str:
        title = heading.group(1)
        words = title.split()

        for i, word in enumerate(words):
            for token in tokens:
                if word.lower() == token.lower() and word != token:
                    print(f"Replacing {word} with {token}")
                    words[i] = token

        return " ".join(words)

    return _


if __name__ == "__main__":
    tokens = []

    for file in VAULT.rglob("*.md"):
        with file.open("r", encoding="utf-8") as f:
            content = f.read()
            tokens.extend(find_acronyms(content))
            tokens.extend(find_compound(content))

    tokens = list(set(tokens))

    csv_print(tokens)

    for file in NEW_VAULT.rglob("*.md"):
        with file.open("r", encoding="utf-8") as f:
            content = f.read()

            heading_pattern = re.compile(r"^#+ (.*)", re.MULTILINE)
            content = heading_pattern.sub(fix_token(tokens), content)

        # with file.open("w", encoding="utf-8") as f:
        #     f.write(content)
