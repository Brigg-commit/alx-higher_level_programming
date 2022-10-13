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

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >=0')
            else:
                self.__size = size

                def area(self):
                    """
                    calculate the area of square
                    Returns:
                     the area of the square
                    """

                    return (self._size) ** 2
