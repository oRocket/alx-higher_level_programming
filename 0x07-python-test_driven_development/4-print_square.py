#!/usr/bin/python3
"""
Module print_square
Prints a square with the character #.
"""


def print_square(size):
    """
    Print a square of '#' characters with the given size.

    :param size: An integer representing the size of the square.

    :raises TypeError: If size is not an integer or is a float and less than 0.
    :raises ValueError: If size is less than 0.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        for b in range(size):
            print('#', end='')
        print()
