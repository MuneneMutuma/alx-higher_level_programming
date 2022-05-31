#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        val = ord(letter)
        if val > 96 and val < 123:
            letter = chr(val - 32)
        print("{}".format(letter), end="")
    print("")
