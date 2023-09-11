#!/usr/bin/python3
# 7-base_geometry.py

"""Module for 7-base_geometry.py"""


class BaseGeometry:
    """definition of class 'BaseGeometry' """
    def __init__(self):
        """Class initialization"""

    def area(self):
        """definition of instance method 'area' """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Definition of function that validates an value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
