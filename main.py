import re


def email_check(email: str) -> bool:
    """Функция проверяющая email."""
    pattern_re = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
    pattern = re.compile(pattern_re)
    if not re.match(pattern, email):
        result = False
    elif not pattern_re:
        result = False
    else:
        result = True
    return result
