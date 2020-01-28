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
