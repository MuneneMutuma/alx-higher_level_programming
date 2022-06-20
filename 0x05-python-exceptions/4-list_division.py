#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    ans_list = list()

    while (i < list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
        except IndexError:
            print("out of range")
            ans_list.append(0)
            i += 1
            continue
        try:
            c = a/b
            ans_list.append(c)
        except ZeroDivisionError:
            print("division by zero")
            ans_list.append(0)
        except (ValueError, TypeError):
            print("wrong type")
            ans_list.append(0)
        i += 1

    return ans_list
