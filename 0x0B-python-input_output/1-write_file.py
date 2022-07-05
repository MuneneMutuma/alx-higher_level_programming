#!/usr/bin/python3
"""A module that writes to a file
"""


def write_file(filename="", text=""):
    """A function that writes to a file

    Attributes:
        filename (str): filename to be opened
        text (str): text to be written to file

    Returns:
        chars (int): number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        chars = f.write(text)

    return(chars)
