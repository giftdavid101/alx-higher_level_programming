#!/usr/bin/python3
"""base class"""


class Base:
    """class definition of Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def __del__(self):
        Base.__nb_objects -= 1h
