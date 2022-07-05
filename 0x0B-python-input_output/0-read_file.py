#!/usr/bin/python3
"""A module for opening a file
"""


def read_file(filename=""):
    """reads a file with `filename`

    Attributes:
        filename (str): file name
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
