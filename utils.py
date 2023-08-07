from pathlib import PurePath


def remove_uuid(file: PurePath) -> PurePath:
    file = PurePath(file)

    parent, stem, suffix = file.parent, file.stem, file.suffix

    clean = PurePath()

    for component in parent.parts:
        component = try_remove_uuid(component)

        clean /= component

    if suffix == ".md":
        stem = try_remove_uuid(file.stem)

    clean /= stem

    return clean.with_suffix(file.suffix)


def try_remove_uuid(component: str) -> str:
    split = component.split()
    code = split[-1]
    if len(code) == 32:
        component = " ".join(split[:-1])

    return component
