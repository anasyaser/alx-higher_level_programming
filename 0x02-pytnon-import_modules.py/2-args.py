#!/usr/bin/python3
from sys import argv

def print_args():
    argv_c = argv[1:]
    n = len(argv_c)

    print("{} arguments".format(n), end="")
    if (n == 0):
        print(".")
    else:
        print(":")

    for i, arg in enumerate(argv_c):
        print("{}: {}".format(i + 1, arg))

if __name__ == "__main__":
    print_args()
