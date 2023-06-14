#!/usr/bin/python3
def weight_average(my_list=[]):
    denom = sum([w * v for w, v in my_list])
    numin = sum([v for w, v in my_list])
    return denom / numin
