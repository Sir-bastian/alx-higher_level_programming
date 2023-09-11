#!/usr/bin/python3
# 8-rectangle.py
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" A module with Rectangle class that inherits from BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Definition of Rectangle class"""
    def __init__(self, width, height):
        """instantiation of class Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
