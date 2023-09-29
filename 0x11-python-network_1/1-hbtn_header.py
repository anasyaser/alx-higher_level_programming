#!/usr/bin/python3
"""Fetch website header element"""
import urllib.request as request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
