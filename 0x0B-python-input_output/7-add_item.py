#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json
from os import path


def save_to_json_file(my_obj, filename):
    """ Save a Python object to a JSON file """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """ Load a JSON file and return its contents as a Python object """
    if not path.exists(filename):
        return []  """ If the file doesn't exist, return an empty list """
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    """ Check if the JSON file exists and load its contents """
    filename = """ add_item.json """
    items = load_from_json_file(filename)

    """ Add command-line arguments to the list """
    items.extend(sys.argv[1:])

    """ Save the updated list to the JSON file """
    save_to_json_file(items, filename)
