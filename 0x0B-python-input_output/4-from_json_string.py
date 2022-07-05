#!/usr/bin/python3
"""Module that provides functionality to convert json string to python object
"""
import json


def from_json_string(my_str):
    """converts a json string to python object

    Attr:
        my_str (str: json): json string

    Return:
        python object conversion of my_str
    """
    return (json.loads(my_str))
