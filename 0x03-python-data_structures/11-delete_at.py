#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return None
    elif idx < 0 or idx >= len(my_list):
        return my_list
    else:
        return print(my_list[:idx] + my_list[idx + 1:])
