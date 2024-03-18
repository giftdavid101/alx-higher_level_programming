#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = mylist[0]
    if len(my_list) == 0:
        return None
    else:
        for number in my_list:
            if number > max_value:
                max_value = number
                return max_value
