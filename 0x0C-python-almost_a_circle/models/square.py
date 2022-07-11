#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        return("[Square] ({}) {}/{} - {}"
               .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """int: length of the square"""
        return (self.width)

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the details of square

        Attr:
            *args (list): no keyword argument list
            **kwargs (dict): key-worded argument list
        """
        if (len(args) > 0):
            self.id = args[0]
        if (len(args) > 1):
            self.size = args[1]
        if (len(args) > 2):
            self.x = args[2]
        if (len(args) > 3):
            self.y = args[3]

        if len(args) == 0:
            for key in kwargs:
                if key == "x":
                    self.x = kwargs["x"]
                if key == "y":
                    self.y = kwargs["y"]
                if key == "size":
                    self.size = kwargs["size"]
                if key == "id":
                    self.id = kwargs["id"]

    def to_dictionary(self):
        dictionary = super().to_dictionary()
        dictionary.pop("width", None)
        dictionary["size"] = dictionary.pop("height", None)

        return dictionary
