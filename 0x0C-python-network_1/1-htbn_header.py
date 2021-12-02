#!/usr/bin/python3
"""Sends request to the URL and display val"""


from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        html = response.info()
    print(html.get("X-Request-Id"))
