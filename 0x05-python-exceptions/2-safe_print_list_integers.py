#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for z in range(x)
    try:
        print("{:d}".format(my_list[z]), end="")
        count += 1
    except (TypeError, ValueError):
        conutinue
        print()
        return count
