def converter(changedstr: str) -> str:
    if not changedstr.endswith("!"):
        changedstr = changedstr + "!"
    return changedstr.capitalize()
