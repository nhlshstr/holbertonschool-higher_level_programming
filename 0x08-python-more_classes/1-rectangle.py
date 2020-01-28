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
