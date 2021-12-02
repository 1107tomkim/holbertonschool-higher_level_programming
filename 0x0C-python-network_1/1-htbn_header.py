#!/usr/bin/python3
"""Sends request to the URL and display val"""


import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        html = response.info()
    print(html.get("X-Request-Id"))
