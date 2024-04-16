#!/usr/bin/python3
"""append_write module to a file"""

def append_write(filename="", text=""):
    """
    A function
    write_file - appends a string at the end of a text file (UTF8),
                and returns the number of characters added:
    Args:
        filename: name of the file
        text: text to be written
    Return: number of bytes written.
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))
