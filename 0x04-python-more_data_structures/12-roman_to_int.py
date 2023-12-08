#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    str = roman_string
    for i in range(len(str)):
        current_value = rom.get(str[i], 0)
        next_value = rom.get(str[i + 1], 0)if i + 1 < len(str) else 0
        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    return result
