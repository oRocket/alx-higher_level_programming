#!/usr/bin/python3
"""
Module add-integer
Adds two integer together

"""

def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a (int): First integer.
        b (int, optional): Second integer. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
