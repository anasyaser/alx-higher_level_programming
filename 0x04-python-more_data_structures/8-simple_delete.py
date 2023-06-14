#!/usr/bin/python3
def simple_delete(a_dict, key=""):
    if key in a_dict:
        del a_dict[key]
    return a_dict


if __name__ == "__main__":
    a = {'language': 'c', 'number': 89, 'track': "low level"}

    new_dict = simple_delete(a, 'track')
    new_dict = simple_delete(a)
    print(new_dict)
    new_dict = simple_delete(a, 'cisfun')
    print(a)
