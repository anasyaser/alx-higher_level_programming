#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    denom = sum([w * v for w, v in my_list])
    numin = sum([v for w, v in my_list])
    return denom / numin
