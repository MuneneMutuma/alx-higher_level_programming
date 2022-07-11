#!/usr/bin/python3
"""Module that implements the `Base` class"""
import json


class Base:
    """Base class for geometry shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of `list_dictionary`"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves dictionary representation of objects to file

        Attr:
            list_objs:`obj`:list of `Base` objects
        """
        if list_objs is None:
            with open(str(cls) + ".json", "w") as f:
                f.write("[]")

        store = list()
        for obj in list_objs:
            store.append(obj.to_dictionary())

        filename = str(cls.__name__) + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(store))
