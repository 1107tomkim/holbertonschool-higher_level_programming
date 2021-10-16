#!/usr/bin/python3
"""Appends string to EOF and return num of chars appended"""


def append_write(filename="", text=""):
    """Appends string to EOF and return num of chars appended"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
