#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    def find_peak_recursive(low, high):
        if low == high:
            return low
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            return find_peak_recursive(low, mid)
        else:
            return find_peak_recursive(mid + 1, high)
    return list_of_integers[find_peak_recursive(0, len(list_of_integers) - 1)]
