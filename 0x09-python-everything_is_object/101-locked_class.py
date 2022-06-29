#!/usr/bin/python3

class LockedClass:
    def __setattr__(self, attribute, value):
        if attribute != "first_name":
            raise AttributeError("'{}' object has no attribute '{}'".format(
                                    self.__class__.__name__, attribute))
        else:
            super().__setattr__(attribute, value)
