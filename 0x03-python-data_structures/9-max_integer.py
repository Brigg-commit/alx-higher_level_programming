#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return
    biggest_value = max_integer(list)
    for k in range(1, length):
        if my_list[k] > biggest_value:
            biggest_value = my_list[k]
        else:
            continue
        return (biggest_value)
