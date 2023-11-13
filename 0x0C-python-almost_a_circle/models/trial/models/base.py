#!/usr/bin/python3

"""Defnes a base class model"""


class Base:
    """
    Base model
    This is the 'base' for all other classes in project 0x0C*.

    Private Class Attribute:  __nb_objects (int), initialized to 0.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialise id
        increment __nb_objects and assign the new value to the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
