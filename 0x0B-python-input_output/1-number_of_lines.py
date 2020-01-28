#!/usr/bin/python3
""" Module with read_file function """


def number_of_lines(filename=""):
    """Function returns number of lines"""
    j = 0
    with open(filename) as f:
        for i in f:
            j += 1
    return j
