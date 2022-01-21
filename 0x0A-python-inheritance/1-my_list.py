#!/usr/bin/python3
"""class tat prints sorted list"""


class MyList(list):
    """prints a list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
