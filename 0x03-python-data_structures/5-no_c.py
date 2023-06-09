#!/usr/bin/python3
def no_c(my_string):
    str_lst = list(my_string)
    return ''.join([char for char in str_lst if char not in "cC"])
