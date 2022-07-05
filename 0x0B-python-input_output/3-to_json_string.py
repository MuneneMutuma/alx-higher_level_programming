#!/usr/bin/python3
"""Module that provides conversion of object to json string functionality
"""
import json


def to_json_string(my_obj):
    """a function that converts object to json

    Attribute:
        my_obj (`obj`): a python object

    Return:
        json format of object
    """
    return (json.dumps(my_obj))
