from pathlib import PurePath


def remove_uuid(file: PurePath) -> PurePath:
    file = PurePath(file)

    parent, stem, suffix = file.parent, file.stem, file.suffix

    clean = remove_folder_uuid(parent)

    if suffix == ".md":
        stem = try_remove_uuid(file.stem)

    clean /= stem

    return clean.with_suffix(file.suffix)


def remove_folder_uuid(folder: PurePath) -> PurePath:
    clean = PurePath()

    for component in folder.parts:
        component = try_remove_uuid(component)

        clean /= component

    return clean


def try_remove_uuid(component: str) -> str:
    split = component.split()
    code = split[-1]
    if len(code) == 32:
        component = " ".join(split[:-1])

    return component
