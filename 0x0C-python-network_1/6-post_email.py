#!/usr/bin/python3
"""Display body of response"""


import requests
from sys import argv


if __name__ == "__main__":
    dict = {}
    dict['email'] = argv[2]
    request = requests.post(argv[1], dict)

    print(request.text)
