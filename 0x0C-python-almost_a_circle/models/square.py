#!/usr/bin/pyhton3
# - square
from models.rectangle import Rectangle

""" Module for square class """


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of 'Square' class.
        init - initilizer
        Args:
            size: size of the square
            x: x position of the square
            y: y position of the square
            id: id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getters for size """
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
