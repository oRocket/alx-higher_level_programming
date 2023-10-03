#!/usr/bin/python3
def remove_char_at(str, n):
    j = 0
    new_str = ""
    for ch in str:
        if j != n:
            new_str += ch
        j += 1
    return new_str
