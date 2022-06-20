#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    while (i < x):
        try:
            val = my_list[i]
        except IndexError:
            print("")
            return count

        try:
            print("{:d}".format(val), end="")
            count += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print("")
    return count
