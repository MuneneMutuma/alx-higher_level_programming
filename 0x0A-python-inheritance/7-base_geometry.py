#!/usr/bin/python3
"""A module that creates an empty class BasicGeometry
"""


class BaseGeometry:
    """Class that implements basic area method
    """
    def area(self):
        """method that raises Exception when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method for validating a value

        Attributes:
            name (str): name
            value (int): integer value

        Raise:
            TypeError: if value is not int
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
