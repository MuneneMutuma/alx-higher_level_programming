#!/usr/bin/python3

"""Module that provides method to look up list of attributes and methods
"""

    
def lookup(obj):
    """looks up the attributes and methods of class

    Attr:
        obj: object
    """
    return (dir(obj))
