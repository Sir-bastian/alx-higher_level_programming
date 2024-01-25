#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Return a peak in alist of unsorted integers"""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    midp = int(size / 2)
    peak = list_of_integers[midp]
    if peak > list_of_integers[midp - 1] and peak > list_of_integers[midp + 1]:
        return peak
    elif peak < list_of_integers[midp - 1]:
        return find_peak(list_of_integers[:midp])
    else:
        return find_peak(list_of_integers[midp + 1:])
