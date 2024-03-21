#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary != 0:
        sorted_keys = sorted(a_dictionary.keys())
        for k in sorted_keys:
            print("{:s}: {}".format(k, a_dictionary[k]))
