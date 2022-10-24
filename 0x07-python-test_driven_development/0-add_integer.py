#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        Type Error: If either of a or b is a non-integer and non-float.
    """
    if type(a) in [int, float]:
        try:
            a = int(a)
            raise TypeError('a must be an integer')
    finally:
        raise TypeError('a must be an integer')

    if type(b) in [int, float]:
        try:
            b = int(b)
            raise TypeError('b must be an integer')
    else:
        raise TypeError('b must be an integer')

    return a + b
