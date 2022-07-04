#!/usr/bin/python3
"""A Module that checks if an object is type of a class
"""


def is_kind_of_class(obj, a_class):
    """function that checks whether an object is of type class

    Attributes:
        obj (obj): object to be checked
        a_class (type): type or class to be checked against

    Return:
        True: if obj is an instance of a_class, else False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
