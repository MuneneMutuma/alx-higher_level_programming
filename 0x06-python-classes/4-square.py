#!/usr/bin/python3
"""A module that describes Square class with size attribute
"""


class Square:
    """This is an empty class for `Square`
    """

    def __init__(self, size=0):
        """Initializer method for the class `Square`.

        Args:
            size: size of the square
                  size should be greater than or equal to zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """Method to find area of a `Square` object
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """A method to retrieve size attr of the instance of `Square`
        """
        return self.__size

    def size(self, value):
        """A setter method to set the value of size for `Square`

        Args:
            value: new value for size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
