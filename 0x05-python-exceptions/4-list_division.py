#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    length = []
    while count < list_length:
        try:
            res = my_list_1[count] / my_list_2[count]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except (TypeError, ValueError):
            res = 0
            print("wrong type")
        except IndexError:
            print("out of range")
            res = 0
        finally:
            count += 1
            length.append(res)
            return length
