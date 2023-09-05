#!/usr/bin/python3
# 2-rectangle.py

"""
A rectangle class representation
"""


class Rectangle:
    """Rectngle class definition"""
    def __init__(self, width=0, height=0):
        """class initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for private instance attribute width"""
        self.__width = value
    if type(value) is not int:
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")

    @property
    def height(self):
        """private instance attribute for height"""
        return self.__height

    @height.setter
    """setter for private instance attribute height"""
    def height(self, value):
        self.__height = value
    if type(value) is not int:
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")

    def area(self):
        """public instance for area calculation"""
        return self.width * self.height

    def perimeter(self):
        perimeter = 2 * self.width + self.height
        if width or height ==  0:
            perimeter = 0
