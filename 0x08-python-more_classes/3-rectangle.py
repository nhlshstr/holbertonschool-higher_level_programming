#!/usr/bin/python3
"""
Module for rectangle
"""


class Rectangle:

    def __init__(self, width=0, height=0):
        """ Instantiation """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Property decorator """
        return self.__width

    @property
    def height(self):
        """ Proeprty decorator for height """
        return self.__height

    @width.setter
    def width(self, value):
        """ Width setter """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Height setter """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ Area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Perimeter of rectangle """
        if (self.width or self.height) == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        lines = ""
        for x in range(self.height):
            lines += "#" * self.width + ("\n" if x != self.height - 1 else "")
        return lines

    def print(self):
        return str(self)
