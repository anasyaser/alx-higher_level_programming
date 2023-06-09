#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_a = (tupla_a[0], 0)
    elif len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        tuple_b = (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    print(add_tuple(tuple_a, tuple_b))
    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))
