#!/usr/bin/python3
"""definition for derived class My list"""


class MyList(list):
    """defines a subclass of list"""
    def print_sorted(self):
        """custom method to sort and print a list"""
        self.sort()
        print(self)


