#!/usr/bin/python3
"""Class square definition"""


class Square:
    """Represent class Square"""

    def __init__(self, size=0):
        """
        Initializes a square
        Args:
            size: size of a square
        Returns:
            None
        """

        if not isinstance(size, int):
                raise TypeError('size must be an integer')
        elif size < 0:
            raise TypeError('size must be >= 0')
        self.__size = size

        def area(self):
            """calculate the area of square
             Returns:
                 the area of the square"""
            return (self.__size * self.__size)
