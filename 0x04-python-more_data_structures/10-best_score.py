#!/usr/bin/python3
def best_score(a):
    if not a:
        return
    return dict([(v, k) for (k, v) in a.items()]).get(max(a.values()))
