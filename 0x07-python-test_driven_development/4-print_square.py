#!/usr/bin/python3
# 4-print_square.py

"""The print_square module which takes one argument"""


def print_square(size):
    """
    definition of print_square function
    that prints a square of lenght size
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float:
        if size < 0:
            raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
