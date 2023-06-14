#!/usr/bin/python3
from functools import reduce


def roman_to_int_v2(roman_string):
    if not roman_string:
        return 0
    roman_int_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10,
                      'V': 5, 'I': 1}
    result = [roman_int_dict.get(sym) for sym in roman_string]
    if None in result:
        return 0
    return reduce(lambda x, y: x + y if y <= x else y - x, result)


if __name__ == "__main__":
    print("X=", roman_to_int_v2("X"))
    print("VII=", roman_to_int_v2("VII"))
    print("IX=", roman_to_int_v2("IX"))
    print("LXXXVII=", roman_to_int_v2("LXXXVII"))
    print("DCCVII=", roman_to_int_v2("DCCVII"))
    print("None=", roman_to_int_v2(None))
    print("ALXVII=", roman_to_int_v2("ALXIVII"))
