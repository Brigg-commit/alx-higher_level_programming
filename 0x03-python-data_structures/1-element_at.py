#!/usr/bin/python3
# funtion that retrieves an element from a list in C
def replace_in_list(my_list, idx):
    if 0 <= idx < len(my_list):
        return my_list[idx]
    return None
