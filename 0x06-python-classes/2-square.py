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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
