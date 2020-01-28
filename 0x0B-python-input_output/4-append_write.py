#!/usr/bin/python3
"""Contains function to append to the end of the file"""


def append_write(filename="", text=""):
    """Function appends text"""
    with open(filename, "a") as f:
        return(f.write(text))
