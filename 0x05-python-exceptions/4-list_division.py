#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    va = 0
    length = []
    while va < list_length:
        try:
            res = my_list_1[va] / my_list_2[va]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
            except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            va += 1
            length.append(res)
    return length
