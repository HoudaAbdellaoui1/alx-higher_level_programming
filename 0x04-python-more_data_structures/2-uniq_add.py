#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set()
    for element in my_list:
        unique_numbers.add(element)

    return sum(unique_numbers)
