#!/usr/bin/python3
def multiply_by_2(a_dict):
    if a_dict:
        return dict([(k, v * 2) for k, v in a_dict.items()])
