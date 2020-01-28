#!/usr/bin/python3
"""Writes to object file in JSON"""
from json import dump


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as op:
        return dump(my_obj, op)
