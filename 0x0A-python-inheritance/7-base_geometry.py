#!/usr/bin/python3
# 7-base_geometry.py

"""Module for 7-base_geometry.py"""


#!/usr/bin/python3
# 5-base_geometry.py

"""Module with an empty cclass BaseGeometry"""


class BaseGeometry:
    """definition of class 'BaseGeometry' """
    def __init__(self):
        """Class initialization"""

    def area(self):
        """definition of instance method 'area' """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
