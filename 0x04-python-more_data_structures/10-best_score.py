#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    ans = list(a_dictionary.keys())[0]
    largest = a_dictionary[ans]
    for key in a_dictionary:
        if a_dictionary[key] > largest:
            ans = key
    return ans
