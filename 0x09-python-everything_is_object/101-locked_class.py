#!/usr/bin/python3
"""Module that implements a simple LockedClass
"""


class LockedClass:
    """Class that allows only an attribute called "first_name"
    """
    def __setattr__(self, attribute, value):
        """override superclass method __setattr__
        """
        if attribute != "first_name":
            raise AttributeError("'{}' object has no attribute '{}'".format(
                                    self.__class__.__name__, attribute))
        else:
            super().__setattr__(attribute, value)
