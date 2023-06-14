#!/usr/bin/python3
def print_sorted_dictionary(a_dict):
    print('\n'.join([f'{key}: {val}' for key, val in sorted(a_dict.items())]))
