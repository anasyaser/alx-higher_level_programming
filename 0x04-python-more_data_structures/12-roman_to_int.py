#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_int_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10,
                      'V': 5, 'I': 1}
    if not roman_string:
        return 0
    result = [0]
    for sym in roman_string:
        cur = roman_int_dict.get(sym)
        if not cur:
            result.append(0)
        elif cur <= result[-1]:
            result.append(cur)
        else:
            result.append(cur - result.pop())
    return sum(result)
