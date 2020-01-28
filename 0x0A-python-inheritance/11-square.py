#!/usr/bin/python3
'''Module with subclass for Square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass of rectangle"""
    def __init__(self, size):
        """Initialization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Implementation for square area"""
        return self.__size ** 2

    def __str__(self):
        """__str__ method"""
        return ("[Square]" + str(self.__size) + "/" + str(self.__size))
