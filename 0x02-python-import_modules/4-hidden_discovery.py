#!/usr/bin/python3
import hidden_4


def print_all_names():
    names = dir(hidden_4)
    for name in names:
        if (name.startswith("__")):
            continue
        print(name)


if __name__ == "__main__":
    print_all_names()
