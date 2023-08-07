from pathlib import Path
import zipfile

from converter import Converter

SRC: zipfile.Path = zipfile.Path("export.zip")
DEST: zipfile.Path = Path("Vault")


def main():
    Converter(SRC, DEST).convert()


if __name__ == "__main__":
    main()
