#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        digit = number % 10
    else:
        digit = number % -10
        digit *= -1
        print("{:d}".format(digit), end='')
        return (digit)
