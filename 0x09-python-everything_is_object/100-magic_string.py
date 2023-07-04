#!/usr/bin/python3
def magic_string(lst=[]):
    lst.append("BestSchool")
    return ",".join(lst)


for i in range(4):
    print(magic_string())
