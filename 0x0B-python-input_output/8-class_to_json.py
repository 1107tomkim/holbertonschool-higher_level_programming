#!/usr/bin/python3
"""Module that returns dict"""


def class_to_json(obj):
    """Returns dict description as JSON"""
    return obj.__dict__
