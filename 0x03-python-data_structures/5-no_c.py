#!/usr/bin/python3

def no_c(my_string):
    i = 0
    ans = str()
    while i < len(my_string):
        if my_string[i] != 'c' and my_string[i] != 'C':
            ans += my_string[i]
        i += 1
    return ans
