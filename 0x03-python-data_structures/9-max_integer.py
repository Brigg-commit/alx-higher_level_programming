#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        largest_value = max_integer(list)
    for k in range(1, length):
        if my_list[k] > largest_value:
            return (largest_value)
