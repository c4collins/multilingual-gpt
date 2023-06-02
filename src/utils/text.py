def urlsafe(unsafe: str) -> str:
    return "-".join(unsafe.split(" ")).lower()
