#!/usr/bin/python3
"""returns object repped by JSON string"""

import json


def from_json_string(my_str):
    """returns object repped by JSON string"""
    return json.loads(my_str)
