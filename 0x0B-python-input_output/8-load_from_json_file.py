#!/usr/bin/python3
"""Creates object from JSON file"""
from json import load


def load_from_json_file(filename):
    """Loads object from JSON"""
    with open(filename, "r", encoding="utf-8") as jfile:
        return load(jfile)
