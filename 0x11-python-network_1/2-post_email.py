#!/usr/bin/python3
"""Fetch website header element"""
import urllib.request as request
import urllib.parse as parser
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = parser.urlencode(value)
    data = data.encode()
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf8'))
