#!/usr/bin/python3
"""
Module for JSON serializations
"""


def class_to_json(obj):
    """JSON serialization"""
    return obj.__dict__
