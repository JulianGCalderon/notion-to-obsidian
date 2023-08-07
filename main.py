import zipfile

from extractor import Extractor

EXPORT: zipfile.Path = zipfile.Path("export.zip")


def main():
    root = Extractor(EXPORT).extract()
    # formatator(root).format()


if __name__ == "__main__":
    main()
