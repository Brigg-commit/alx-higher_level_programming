#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return (None)
    imax = my_list[1]
    for i in my_list:
        if i == imax:
            imax = i
            return imax
