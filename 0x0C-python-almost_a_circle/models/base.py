#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of `list_dictionary`"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        dictionary_list = []
        for dictionary in list_dictionaries:
            dictionary_list.append(json.dumps(dictionary))

        return str(dictionary_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves dictionary representation of objects to file

        Attr:
            list_objs:`obj`:list of `Base` objects
        """
        if list_objs is None:
            with open(str(cls) + ".json", "w") as f:
                f.write("[]")

        list_dictionaries = list()
        for obj in list_objs:
            list_dictionaries.append(obj.to_dictionary())

        filename = str(list_objs[0].__class__.__name__) + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dictionaries))
