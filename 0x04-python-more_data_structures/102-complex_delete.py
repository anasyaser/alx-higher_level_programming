#!/usr/bin/python3
def complex_delete(a_dict, value):
    if not a_dict:
        return
    result = []
    for k, v in a_dict.items():
        if v == value:
            result.append(k)
    for k in result:
        del a_dict[k]
    return a_dict
