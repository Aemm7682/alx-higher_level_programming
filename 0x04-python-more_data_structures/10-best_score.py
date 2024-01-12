#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val_max = 0
    key_max = ""
    for x, y in a_dictionary.items():
        if y > val_max:
            val_max = y
            key_max = x
    return key_max
