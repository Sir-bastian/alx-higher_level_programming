#!/usr/bin/python3
# 0-lookup.py

""" This is a module with a function that returns the list
of available attributes and metods of an object"""


def lookup(obj):
    """
    Definition of lookup function that return a list objects
    """
    return dir(obj)
