#!/usr/bin/python3
# 2-rectangle.py

"""
A rectangle class representation
"""


class Rectangle:
    """Rectngle class definition"""

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """class initialization"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a message when an instance is deleted"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter for private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for private instance attribute width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance attribute for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter definition for private instance attribute
        height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance for area calculation"""
        area = self.width * self.height
        return area

    def perimeter(self):
        perimeter = (self.width + self.height) * 2
        if self.width == 0:
            perimeter = 0
        if self.height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
