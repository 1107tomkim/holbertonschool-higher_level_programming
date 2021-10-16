#!/usr/bin/python3
"""prints txt files to stdout after reading"""


def read_file(filename=""):
    """prints txt files to stdout after reading"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
