#!/usr/bin/python3
"""
Module for rectangle
"""


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 == rect_2:
            return rect_1
        return rect_1 if rect_1.area() > rect_2.area() else rect_2

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
        """ Str method """
        lines = ""
        for x in range(self.height):
            lines += str(Rectangle.print_symbol) * self.width + (
                    "\n" if x != self.height - 1 else "")
        return lines

    def print(self):
        """ Print function """
        return str(self)

    def __repr__(self):
        """ Repr method """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
