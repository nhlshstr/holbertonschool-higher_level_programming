#!/usr/bin/python3
"""Consists class student"""


class Student:
    """JSONified class with student"""
    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts from dictionary"""
        return self.__dict__.copy()
