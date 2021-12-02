#!/usr/bin/python3
"""Sends request to URL and display body"""


from urllib import request, parse, error
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
        except error.HTTPError as e:
            print("Error code: {}".format(e.code))
