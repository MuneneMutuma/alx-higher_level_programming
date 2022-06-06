#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    ans = list()
    for i in my_list:
        if i % 2 == 0:
            ans.append(True)
            continue
        ans.append(False)
    return ans
