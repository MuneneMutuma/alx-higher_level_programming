#!/usr/bin/python3
"""A module that implements `Rectangle`
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method for Rectangle"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """property method for width:

        """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """property method for height:

        """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def x(self):
        """property method for x:

        """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be => 0")
        self.__x = x

    @property
    def y(self):
        """property method for y:

        """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be => 0")
        self.__y = y

    def area(self):
        """finds area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays A rectangle using #"""
        i = 0
        print("{}".format("\n" * self.__y), end="")
        while (i < self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))
            i += 1

    def __str__(self):
        """Overide string representation of the Rectangle"""
        return("[Rectangle] ({}) {}/{} - {}/{}"
               .format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def update(self, *args, **kwargs):
        """updates `Rectangle`"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

        if len(args) == 0:
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "id" in kwargs:
                self.id = kwargs["id"]

    def to_dictionary(self):
        """returns dictionary representation of Rectangle object"""
        dictionary = dict()

        dictionary["id"] = self.id
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        dictionary["width"] = self.width
        dictionary["height"] = self.height

        return dictionary
