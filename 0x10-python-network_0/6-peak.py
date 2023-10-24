#!/usr/bin/python3
"""
Find the peak of list
"""
def find_peak(lst):
    """Find the peak of list"""
    length = len(lst)
    idx = length // 2
    if (length == 0):
        return
    if (length == 1):
        return lst[0]
    if (idx + 1 < length) and lst[idx+1] > lst[idx]:
        return find_peak(lst[idx+1:])
    elif (idx - 1 > -1) and lst[idx-1] > lst[idx]:
        return find_peak(lst[:idx])
    elif (idx - 1 > -1) and (idx + 1 < length) and\
         (lst[idx] == lst[idx-1] == lst[idx+1]):
        return max(find_peak(lst[:idx]), find_peak(lst[idx+1:]))
    else:
        return lst[idx]
