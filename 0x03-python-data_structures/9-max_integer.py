#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return
    biggest_value = my_list([0])
    for k in range(1, length):
        if my_list[k] > biggest_value:
            biggest_int = my_list[k]
            return (biggest_value)
