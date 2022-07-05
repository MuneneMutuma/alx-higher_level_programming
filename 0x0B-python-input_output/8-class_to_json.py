#!/usr/bin/python3
"""Module for converting class a data to json object
"""


def class_to_json(obj):
    """function that converts class attributes to json

    Attr:
        obj (`obj`): python object

    Return:
        json object
    """
    return (obj.__dict__)
