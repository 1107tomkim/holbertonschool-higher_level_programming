#!/usr/bin/python3
""" Defines class BaseGeometry"""


class BaseGeometry:
    "Class BaseGeometry"

    def area(self):
        """Raise exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be great than 0".format(name))
