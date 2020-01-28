#!/usr/bin/python3
"""
Consists of class base geometry
"""


class BaseGeometry:
    """ Class BaseGeometry """

    def area(self):
        """
        Function area() that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates int values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
