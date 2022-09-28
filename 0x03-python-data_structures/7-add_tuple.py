#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = []
    new_tuple_b = []
    result = []
    # check for tuple-a
    new_tuple_a = list(tuple_a)
    new_tuple_a = list(tuple_b)
    if len(new_tuple_a) < 2:
        for x in range(2 - len(new_tuple_a)):
            new_tuple_a.append(0)
            if len(new_tuple_b) < 2:
                for y in range(2 - len(new_tuple_b)):
                    new_tuple_b.append(0)
                    for z in range(2):
                        result.append(new_tuple_a[x] + new_tuple_b[x])
                        return tuple(result)
