#!/usr/bin/python3
"""Module that checks if an object inherits from a class
"""


def inherits_from(obj, a_class):
    """function that checks if obj is an instance of a_class that is inherited

    Attributes:
        obj (object): object
        a_class (type): type which is to be checked against

    Return:
        True: if object is an instance of a_class that is inherited from it
        False: otherwise
    """
    if issubclass(obj.__class__, a_class) and not type(obj) is a_class:
        return True
    else:
        return False
