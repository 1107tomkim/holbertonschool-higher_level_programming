#!/usr/bin/python3
"""Writes a string and counts num of char of a string"""


def write_file(filename="", text=""):
    """Writes a string and counts num of char of a string"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
