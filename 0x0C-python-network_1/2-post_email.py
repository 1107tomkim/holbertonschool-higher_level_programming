#!/usr/bin/python3
"""Takes URL and Email and sends a post request"""


from urllib import request, parse, error
from sys import argv


if __name__ == "__main__":
    dict = {}
    dict['email'] = argv[2]
    data = parse.urlencode(dict)
    data = data.encode('utf-8')
    with request.urlopen(argv[1], data) as response:
        html = response.read()
        print(html.decode('utf-8))
