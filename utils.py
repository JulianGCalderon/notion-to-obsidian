from pathlib import PurePath


def remove_uuid(file: PurePath) -> PurePath:
    file = PurePath(file)
    print(file)

    clean = remove_folder_uuid(file.parent)

    if file.suffix == ".md":
        clean /= try_remove_uuid(file.stem)
        clean = clean.with_suffix(file.suffix)

    return clean


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
