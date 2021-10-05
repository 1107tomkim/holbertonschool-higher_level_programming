#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ndictionary = a_dictionary.copy()
    for x in sorted(ndictionary):
        print("{}: {}".format(x, ndictionary[x]))
