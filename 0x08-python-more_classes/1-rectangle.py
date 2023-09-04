#!/usr/bin/python3
# 1-rectangle.py

"""A Rectangle class definition"""


class Rectangle:
    """ A class that represents a rectangle """
    def ___init__(self, width=0, height=0):
        """rectangle initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """private attribute width setter"""
        if type(value) is not int:
            raise TypeError("width must be an intger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private nstance atribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
