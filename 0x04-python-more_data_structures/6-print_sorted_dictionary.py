#!/usr/bin/python3
def print_sorted_dictionary(a_dict):
    if (a_dict):
        print('\n'.join([f'{k}: {v}' for k, v in sorted(a_dict.items())]))
