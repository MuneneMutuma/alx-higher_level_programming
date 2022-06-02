#!/usr/bin/python3

import sys


def main():
    args = sys.argv
    i = 1

    if len(args) == 1:
        print("0 arguments.")
    elif len(args) == 2:
        print("1 argument:")
        print("1: {}".format(args[1]))
    else:
        print("{} arguments:".format(len(args) - 1))
        while i < len(args):
            print("{}: {}".format(i, args[i]))
            i += 1


if __name__ == "__main__":
    main()
