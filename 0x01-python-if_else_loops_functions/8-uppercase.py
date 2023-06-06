#!/usr/bin/python3
def uppercase(str):
    nstr = ''
    for char in str:
        if (97 <= ord(char) <= 123):
            nstr += chr(ord(char) - 32)
        else:
            nstr += char
    print("{}".format(nstr))
