#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    double = dict()
    for key in a_dictionary:
        double[key] = a_dictionary[key] * 2
    return double
