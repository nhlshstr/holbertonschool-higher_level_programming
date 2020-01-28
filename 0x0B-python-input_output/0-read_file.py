#!/usr/bin/python3
""" Module with read_file function """


def read_file(filename=""):
    with open(filename) as f:
        for i in f:
            print(i, end="")
