#!/usr/bin/python3
for i in range(9):
    for y in range(i + 1, 10):
        if (i == 8 and y == 9):
            print("{}{}".format(i, y))
            continue
        print("{}{}".format(i, y), end=", ")
