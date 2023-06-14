#!/usr/bin/python3
def print_sorted_dictionary(a_dict):
    if (a_dict):
        print('\n'.join([f'{k}: {v}' for k, v in sorted(a_dict.items())]))


if __name__ == "__main__":
    a_dict = {'lang': 1, 'Number': 98, 'track': "low lweve", 'a': {'c': 1, 'b': 2}}
    print_sorted_dictionary(a_dict)
