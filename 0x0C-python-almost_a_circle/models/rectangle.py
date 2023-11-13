#!/usr/bin/python3
"""
Define the class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    Define the class Rectangle that inherits from Base.

    Private class attributes:
        __width = width
        __height = height
        __x = x
        __y = y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initilising rectangle objects

        Args:
            width (int): The width of the rectangle
            height (int): The height og the rectangle
            x (int): The x coordinate of the rectangle
            y (int): The y coordinate of the rectangle
            id (int): The identity of the rectangle

        Return:
            Always 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
