from pathlib import PurePath


def to_pure_path(path) -> PurePath:
    return PurePath(str(path))


def remove_uuid(file: PurePath) -> PurePath:
    file = to_pure_path(file)
    clean_path = PurePath()

    for component in file.parts[:-1]:
        if component == "..":
            clean_path /= component
            continue

        component = " ".join(component.split()[:-1])

        clean_path /= component

    name = file.parts[-1]
    if file.suffix == ".md":
        name = " ".join(name.split()[:-1])
        name += ".md"

    clean_path /= name

    return clean_path
