#!/usr/bin/python3
incr = 0
for i in range(122, 96, -1):
    print("{}".format(chr(i - (32 * (incr % 2)))), end='')
    incr += 1
