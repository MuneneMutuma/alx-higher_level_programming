#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or None:
	    return 0
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    length = len(roman_string)

    ans = 0
    i = 0
    while i < length:
        current = roman_string[i]
        if i < length - 1:
            ahead = roman_string[i + 1]
            if current == "I" and (ahead == "V" or  ahead == "X"):
                ans -= vals[current]
            elif current == "X" and (ahead == "L" or ahead == "C"):
                ans -= vals[current]
            elif current == "C" and (ahead == "D" or ahead == "M"):
                ans -= vals[current]
            else:
                ans += vals[current]
        else:
            ans += vals[current]
        i += 1
    return ans
