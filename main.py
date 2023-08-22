from pathlib import Path
import argparse
import zipfile

from converter import Converter

SRC: zipfile.Path = zipfile.Path("export.zip")
DEST: zipfile.Path = Path("Vault")

parser = argparse.ArgumentParser(
    prog="Notion to Obsidian converter",
    description="Converts a Notion export to an Obsidian vault.",
    epilog="Made by @juliangcalderon",
)

parser.add_argument(
    "src_path", type=zipfile.Path, help="Notion extract zip source path"
)
parser.add_argument("dest_path", type=Path, help="Obsidian vault destination path")
parser.add_argument(
    "-m",
    "--mathjax",
    type=bool,
    help="Enable MathJax conversion from Katex",
    action=argparse.BooleanOptionalAction,
)


if __name__ == "__main__":
    args = parser.parse_args()
    Converter(args.src_path, args.dest_path, args.mathjax).convert()
