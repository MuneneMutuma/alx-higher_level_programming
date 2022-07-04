#!/usr/bin/python3
"""A module that inherits `list`

The module implements a method to print a sorted list
"""


class MyList(list):
    """MyList class that inherits list and extends functionality
    """
    def print_sorted(self):
        """prints a sorted list
        """
        print(sorted(self))
