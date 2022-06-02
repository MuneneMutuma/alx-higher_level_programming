#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def main():
    args = sys.argv
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if len(args) != 4:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        exit(1)

    if args[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    f = operators.get(args[2])

    a = int(args[1])
    b = int(args[3])
    print("{} {} {} = {}".format(a, args[2], b, f(a, b)))


if __name__ == "__main__":
    main()
