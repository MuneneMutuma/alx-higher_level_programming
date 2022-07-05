#!/usr/bin/python3
"""module that provides function to save json to file
"""
import json


def save_to_json_file(my_obj, filename):
    """a function that saves an object as json to file

    Attr:
        my_obj (`obj`): python object
        filename (str): name of the file
    """
    json_object = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(json_object)
