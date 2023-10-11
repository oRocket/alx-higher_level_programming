#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Check if the key is in the dictionary before attempting to delete it
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
