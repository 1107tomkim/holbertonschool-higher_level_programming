#!/usr/bin/python3
"""Module class student"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """def init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """from dict to json file"""
        return self.__dict__
