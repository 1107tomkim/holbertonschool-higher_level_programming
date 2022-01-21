#!/usr/bin/python3
"""true if its an instance of class else false"""


def is_same_class(obj, a_class):
    """true if instance else false"""
    if type(obj) == a_class:
        return True
    else:
        return False
