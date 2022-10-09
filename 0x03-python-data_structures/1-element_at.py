#!/usr/bin/python3
# funtion that retrieves an element from a list in C
def replace_in_list(my_list, idx):
    if idx < 0:
        return (None)
    length = len(my_list)
    if idx > length - 1:
        return (None)
    return (my_list[idx])
