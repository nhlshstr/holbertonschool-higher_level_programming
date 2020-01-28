#!/usr/bin/python3
class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Position setter
        """
        if (type(value[0] or type(value[1])) != int) or (
                value[1] or value[0]) < 0 or len(value) != 2 or type(value) != tuple

    def area(self):
        """Return area"""
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
