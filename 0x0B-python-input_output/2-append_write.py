#!/usr/bin/python3
"""Module that provides a function to append to a filename
"""


def append_write(filename="", text=""):
    """a function that appends to `filename` with `text`

    Args:
        filename (str): filename onto which to be appended
        text (str): text to be appended to file

    Returns:
        chars (int): number of characters to be written
    """
    with open(filename, "a", encoding="utf-8") as f:
        chars = f.write(text)

    return chars
