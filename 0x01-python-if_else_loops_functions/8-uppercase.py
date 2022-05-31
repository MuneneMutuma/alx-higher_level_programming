#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        val = ord(letter)
        if val > 96 and val < 123:
            uppercase = chr(val - 32)
            print("{}".format(uppercase), end="")
        else:
            print(letter, end="")
    print("")
