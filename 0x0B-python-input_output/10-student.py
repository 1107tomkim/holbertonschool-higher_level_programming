#!/usr/bin/python3
"""Module class student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """def init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """from a dict to a json file"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for at in attrs:
            try:
                new_dict[at] = self.__dict__[at]
            except:
                pass
        return new_dict
