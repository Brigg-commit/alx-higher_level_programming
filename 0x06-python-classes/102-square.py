#!/usr/bin/python3
"""Define square class"""


class Square:
    """Representing the square class"""
    def __init__(self, size=0):
        """Initialized size of the square"""
        self.size = size

    @property
    def size(self):
        """property for the length of the size of the square"""
        return self.__size = size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')         self.__size = value

    def area(self):
        """Area of this square.
        Returns:
            The size squared.
        """
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
