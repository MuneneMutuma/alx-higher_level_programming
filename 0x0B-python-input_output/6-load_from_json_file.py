#!/usr/bin/python3
"""Module provides functionality to create Object form json file
"""
import json


def load_from_json_file(filename):
    """function that creates Object from json file

    Attr:
        filename (str): name of the file

    Return:
        Python Object
    """
    with open(filename, 'r') as f:
        read_data = f.read()

    return(json.loads(read_data))
