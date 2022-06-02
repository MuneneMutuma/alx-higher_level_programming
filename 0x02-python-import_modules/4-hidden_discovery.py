#!/usr/bin/python3.8

import hidden_4


def reveal():
    vals = dir(hidden_4)

    for val in vals:
        if val[0] != '_':
            print(val)


if __name__ == "__main__":
    reveal()
