#!/usr/bin/python3


"""Square class definition"""


class Square:

    """Represents a square
    Attributes:
        __size (int): size of a side a square"""

    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): size of side of the square
          Returns:
          None"""

        self.__size = size:

            @property
            def size(self):
                """getter of --size
                Args:
                    value (int): the size of a size of the square
                Returns:
                None"""
                return (self.__size)

            @size.setter
            def size(self, value):
                """setter of __size
                Args:
            value (int): the size of a size of the square
                Returns:
                None"""
                if not isinstance(value, int):
                    raise TypeError("size must be interger")
                elif value < 0:
                    raise ValueError("size must be >= 0")
                self.__size = value

            def area(self):                                       """calculate the squares of the area
                Returns:                                           the area of the square"""
                return (self.__size * self.__size)
