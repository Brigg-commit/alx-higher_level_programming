#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_l = my_list[:]
    for x in range(0, len(my_list)):
        if my_list[x] % 2 == 0:
            new_l[x] = 1
        else:
            new_[x] = 0
            return (new_l)
