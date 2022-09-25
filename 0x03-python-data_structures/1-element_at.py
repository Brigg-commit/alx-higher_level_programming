#!/usr/bin/python3
def replace_in_list(my_list, idx):
    if idx < 0:
        return (None)
    length = len(my_list)
    if idx > len(my_list) - 1:
        return (None)
    return (my_list[idx])
