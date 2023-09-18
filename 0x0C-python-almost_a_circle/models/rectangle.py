#!/usr/bin/python3
# - rectangle.py
from models.base import Base

""" Module for class Rectangle"""


class Rectangle(Base):
    """ A class rectangle that inheris from Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization of rectangle class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Definition of getter method for width attribute  """
        return self.__width

    @width.setter
    def width(self, width):
        """ Definition of setter method for width attribute """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Definition of getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """ Definiton of setter method for the height attribute """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter method for the x attribute """
        return self.__x

    @x.setter
    def x(self, x):
        """setter method for the x attribute """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter method for  y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """ setter method for the y attribute """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Definition of public method that returns area value
        of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        prints rectangle using the '#' symbol
        """
        for y in range(self.y):
            print()
        for column in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for row in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """ Returns a string representation """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
