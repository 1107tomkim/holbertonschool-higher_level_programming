#!/usr/bin/python3
"""checks if an object is a instance of a class"""


def inherits_from(obj, a_class):
    """checks to see if an object is a instance of a class"""

    return(issubclass(type(obj), a_class) and type(obj) is not a_class)
