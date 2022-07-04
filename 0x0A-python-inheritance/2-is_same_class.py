#!/usr/bin/python3
"""module that checks for class of an object
"""


def is_same_class(obj, a_class):
    """function that checks if an object is of a given type

    Attributes:
        obj (obj): object to be checked for type
        a_class (type): suspected type of obj

    Returns:
        True: if type of object is a_class, else False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
