#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    A function called
    write_file - that writes a string to a text file,
                and returns the number of characters written:
    Return: number of bytes written.
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
