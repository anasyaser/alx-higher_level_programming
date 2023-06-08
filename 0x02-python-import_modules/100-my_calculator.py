#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def check_arguments(args):
    if (len(args) - 1) != 3:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        exit(1)
    elif args[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


def operation(args):
    a = int(args[1])
    b = int(args[3])
    operator = args[2]
    result = 0

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    args = sys.argv
    check_arguments(args)
    operation(args)
