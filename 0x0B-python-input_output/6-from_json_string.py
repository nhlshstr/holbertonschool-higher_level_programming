#!/usr/bin/python3
"""This module is to deserialize JSON object"""
from json import loads


def from_json_string(my_str):
    return(loads(my_str))
