#!/usr/bin/python3
"""Module that implements a class Student
"""


class Student:
    """a `Student` class

    Attr:
        first_name (str): first name
        last_name (str): last name
        age (age): age
    """
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        """constructor method

        Attr:
            first_name (str): first name
            last_name (str): last name
            age (age): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that returns dict object of class attributes and methds

        Returns:
            dictionary of self with all the attributes
        """
        ans = dict()
        if attrs is None:
            return self.__dict__

        for attr in attrs:
            if attr in self.__dict__:
                ans[attr] = self.__dict__[attr]

        return (ans)
