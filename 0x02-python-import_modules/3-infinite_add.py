#!/usr/bin/python3

import sys


def infinite_add():
    args = sys.argv
    i = 1
    sum = 0

    while i < len(args):
        sum += int(args[i])
        i += 1

    print("{}".format(sum))


if __name__ == "__main__":
    infinite_add()
