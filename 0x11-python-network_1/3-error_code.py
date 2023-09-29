#!/usr/bin/python3
"""Print Body content and Handle errors"""
import urllib.request as request
import urllib.error
import sys


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
