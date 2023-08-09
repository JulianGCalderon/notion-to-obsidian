from pathlib import Path
from PIL import Image


VAULT = Path("C:\\Users\\Julian\\Vaults\\Facultad")


def convert_transparent_to_white(src_path, dest_path):
    img = Image.open(src_path)

    img = img.convert("RGBA")

    data = img.getdata()
    new_data = []

    modified = False
    for item in data:
        if item[3] == 0:
            new_data.append((255, 255, 255, 255))
            modified = True
        else:
            new_data.append(item)

    if not modified:
        return

    print("modifying", src_path)

    img.putdata(new_data)

    img.save(dest_path, "PNG")


for png in VAULT.rglob("*.png"):
    convert_transparent_to_white(png, png)
