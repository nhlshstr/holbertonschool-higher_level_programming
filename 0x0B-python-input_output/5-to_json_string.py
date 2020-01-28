#!/usr/bin/python3
"""Module to return object data in JSON"""
from json import dumps


def to_json_string(my_obj):
    """Returns object data in JSON"""
    return dumps(my_obj)
