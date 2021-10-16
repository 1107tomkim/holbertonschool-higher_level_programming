#!/usr/bin/python3
"""creates object from JSON"""


import json


def load_from_json_file(filename):
    """creates object from JSON"""
    with open(filename) as f:
        return json.loads(f.read())
