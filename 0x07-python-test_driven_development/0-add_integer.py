#!/usr/bin/python3


def add_integer(a, b=98):
    """
    A function that adds two numbers.
    Parameters:
    a (int): first number.
    b (int): second number.
    Returns:
    int: The sum of a and b.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)

    return a+b
