#!/usr/bin/python3
"""program to roman number to normal number conversion"""


def roman_to_int(roman_string):
    num = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_int_dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for i in range(len(roman_string)):
        if rom_int_dic.get(roman_string[i], 0) == 0:
            return 0
        if (i != len(roman_string) - 1) and
        rom_int_dic[roman_string[i]] < rom_int_dic[roman_string[i + 1]]:
            num += rom_int_dic[roman_string[i]] * -1
        else:
            num += rom_int_dic[roman_string[i]]

    return num
