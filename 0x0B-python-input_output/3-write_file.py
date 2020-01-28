#!/usr/bin/python3
"""Module with function to write to file"""


def write_file(filename="", text=""):
    """ Function to write 'text' to 'filename' """
    with open(filename, "w") as f:
        return(f.write(text))
