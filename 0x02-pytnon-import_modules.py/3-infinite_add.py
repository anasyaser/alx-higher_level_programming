#!/usr/bin/python3
from sys import argv

def add_args():
    argv_c = argv[1:]
    res = 0

    for arg in argv_c:
        res += int(arg)
    return (res)

if __name__ == "__main__":
    print(add_args())
