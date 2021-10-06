#!/usr/bin/python3
"Module is used to create class square"


class Square:
    "Defines class and instantiates"
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size