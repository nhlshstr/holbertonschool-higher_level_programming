#!/usr/bin/python3
"""
Houses inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """Checks if object is a subclass and
    not the same class
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
