#!/usr/bin/python3
""" JSON API """
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        v = ""
    else:
        v = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': v})
    try:
        j = r.json()
        if j:
            print("[{}] {}".format(j['id'], j['name']))
        else:
            print('No result')
    except Exception as e:
        print("Not a valid JSON")
