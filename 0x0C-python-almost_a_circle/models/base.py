#!/usr/bin/python3
"""Module that implements the `Base` class"""
import json
import csv


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

    @staticmethod
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
            with open(str(cls.__name__) + ".json", "w") as f:
                f.write("[]")
        else:
            store = list()
            for obj in list_objs:
                store.append(obj.to_dictionary())

            filename = str(cls.__name__) + ".json"
            with open(filename, "w") as f:
                f.write(cls.to_json_string(store))

    @staticmethod
    def from_json_string(json_string):
        """Converts json string to list object"""
        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(4, 4)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads and creates objects from file"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as f:
                instances = f.read()
        except FileNotFoundError:
            return []

        dictionary_list = cls.from_json_string(instances)

        result = list()
        for item in dictionary_list:
            result.append(cls.create(**item))

        return(result)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"

        content = []
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]

            for obj in list_objs:
                tmp = []
                tmp_dict = obj.to_dictionary()
                tmp.append(tmp_dict.get("id"))
                tmp.append(tmp_dict.get("width"))
                tmp.append(tmp_dict.get("height"))
                tmp.append(tmp_dict.get("x"))
                tmp.append(tmp_dict.get("y"))

                content.append(tmp)

        if cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]

            for obj in list_objs:
                tmp = []
                tmp_dict = obj.to_dictionary()
                tmp.append(tmp_dict.get("id"))
                tmp.append(tmp_dict.get("size"))
                tmp.append(tmp_dict.get("x"))
                tmp.append(tmp_dict.get("y"))

                content.append(tmp)
        with open(filename, "w") as f:
            csvwriter = csv.writer(f)

            csvwriter.writerow(fields)
            csvwriter.writerows(content)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        result = list()

        try:
            with open(filename, "r") as f:
                instances = csv.DictReader(f)
                for instance in instances:
                    for item in instance:
                        instance[item] = int(instance[item])
                    result.append(cls.create(**instance))
        except FileNotFoundError:
            return []

        return result
