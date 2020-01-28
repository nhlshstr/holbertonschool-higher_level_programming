#!/usr/bin/python3
"""Function to read lines"""


def read_lines(filename="", nb_lines=0):
    """Reads specified number of lines"""
    with open(filename) as f:
        strList = list(f)

    if nb_lines <= 0 or nb_lines >= len(strList):
        for x in strList:
            print(x, end="")
    else:
        for line in range(0, nb_lines):
            print(strList[line], end="")
