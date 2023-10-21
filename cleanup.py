def clean(s):
    """Removes all non-alphabet characters from a string and
    replaces them with a space"""
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news
