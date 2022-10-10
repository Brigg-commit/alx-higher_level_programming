#!/usr/bin/python3
# 'function that returns a new dictionary with all values multiplied by 2'
def multiply_by_2(a_dictionary):
    temp = dict(a_dictionary)
    for key, value in temp.items():
        temp[key] = value * 2
        return temp
