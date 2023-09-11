#!usr/bin/python3
# 1-my_list.py

""" Module for a class 'MyList' that inherits from 'list'."""


class MyList(list):
    """ Definiton of class MyList"""
    def __init__(self):
        """initialization"""

    def print_sorted(self):
        """Public instance that prints the list but sorted"""
        print(sorted(self))
