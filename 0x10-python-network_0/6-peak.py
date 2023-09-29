#!/usr/bin/python3
"""
Find the peak of list
"""
def find_peak(lst):
    """Find the peak of list"""
    idx = len(lst) // 2
    if lst[idx+1] and lst[idx+1] > lst[idx]:
        return find_peak(lst[idx+1:])
    elif lst[idx-1] and lst[idx-1] > lst[idx]:
        return find_peak(lst[:idx])
    elif lst[idx-1] andlst[idx] == lst[idx-1] == lst[idx+1]:
        return max(find_peak(lst[:idx], lst[idx+1:]))
    else:
        return lst[idx]
