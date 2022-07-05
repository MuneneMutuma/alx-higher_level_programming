#!/usr/bin/python
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
        Student.first_name = first_name
        Student.last_name = last_name
        Student.age = age

    def to_json(self):
        """method that returns dict object of class attributes and methds

        Returns:
            dictionary of self with all the attributes
        """
        return Student.__dict__
