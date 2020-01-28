#!/usr/bin/python3
"""
Subclass Rectangle derived from
BaseGeometry
"""
BG = __import__("7-base_geometry").BaseGeometry


class Rectangle(BG):
    """Rectangle - subclass of BaseGeometry"""

    def __init__(self, width, height):
        """Initialized w & h"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implemented area() function"""
        return (self.__width * self.__height)

    def __str__(self):
        """__str__ method"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
