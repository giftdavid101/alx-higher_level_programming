#!/usr/bin/python3

"""Create a class Rectangle that defines a rectangle"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve attribute"""
        return self.__width
    @property
    def height(self):
        """To retrieve attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        """To set attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """To set the attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Get area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Get perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.height + self.width)
