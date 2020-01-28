#!/usr/bin/python3
"""Contains class that inherits list"""


class MyList(list):
    """My list class inherited from list"""
    def print_sorted(self):
        """ Function to print sorted list """
        print(sorted(self))
