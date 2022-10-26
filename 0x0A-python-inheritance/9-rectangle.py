#!/usr/bin/python3
"""Defines a rectangle class using BaseGeometry."""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry)
    """Reprsent rectangle class that inherit from BaseGeometry."""

    def integer_validator(self, width, height):
        """initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.integer_validator(" width", width)
        self.__width = width
        self.integer_validator(" height", height)
        self.__height = height

        def __str__(self)
        """Return the str() representation of a rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):                              """Returns the area of the rectangle"""
    return self.__width * self.__height
