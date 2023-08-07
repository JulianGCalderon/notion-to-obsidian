from pathlib import Path


class formatator:
    def __init__(self, root: Path):
        self.root = root
        pass

    def format(self):
        for file in self.root.rglob("*.md"):
            self.fix_latex(file)

    def fix_latex(self, file: Path):
        pass
