#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    max_num = min(my_list)
    for i in my_list:
        if i > max_num:
            max_num = i
    return max_num
