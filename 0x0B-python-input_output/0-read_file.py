#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=""):
    """Print the contents of a text file(UTF8) to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
