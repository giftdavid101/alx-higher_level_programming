#!/usr/bin/python3

"""Defines a text reading from a file"""


def read_file(filename=""):
    """Reads text from a file and outputs to stdout"""
    with open(filename) as file:
        content = file.read()
    print(content, end="")
