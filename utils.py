import re


def strip_emojis(text: str) -> str:
    return re.sub(r'[^\w\s\d\-_\.,!?;:\'"()\[\]{}@#$%&*+=<>/\\|~`^]', '', text, flags=re.UNICODE).strip()
