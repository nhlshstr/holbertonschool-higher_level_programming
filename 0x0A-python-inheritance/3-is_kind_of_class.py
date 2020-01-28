#!/usr/bin/python3
"""
Module for is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is a part of same class
    or a sub class
    """
    return (isinstance(obj, a_class))
