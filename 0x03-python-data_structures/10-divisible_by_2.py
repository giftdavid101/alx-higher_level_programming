#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    if len(my_list) == 0:
        return None
    else:
        for number in my_list:
            if number % 2 == 0:
                list_result.append(True)
            else:
                list_result.append(False)
        return list_result
