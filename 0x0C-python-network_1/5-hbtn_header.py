#!/usr/bin/python3
"""Sends Request to URL"""


import requests
from sys import argv


if __name__ == "__main__":
    request = requests.get(argv[1])
    data = request.headers

    print(data.get('X-Request-Id'))
