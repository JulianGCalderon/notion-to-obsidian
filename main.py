import zipfile

from extractor import Extractor
from formatator import formatator
from organizer import Organizer

EXPORT: zipfile.Path = zipfile.Path("export.zip")


def main():
    root = Extractor(EXPORT).extract()
    Organizer(root).organize()
    # formatator(root).format()


if __name__ == "__main__":
    main()
