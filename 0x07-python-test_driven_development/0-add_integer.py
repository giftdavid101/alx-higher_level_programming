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
    if type(a) && type(b) is not int and type(a) && type(b) is not float:
        raise TypeError("a and b must be an integer")
    a = int(a)
    b = int(b)


    return a+b;
