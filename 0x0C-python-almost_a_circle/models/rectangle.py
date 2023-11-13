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

        Exceptions:
            If the input is not an integer. raise 
                TypeError: Input must be an integer
            If width or height is under or equals 0, raise
                ValueError: Width or height must be > 0
            If x or y is under 0, raise
                ValueError: x or y must be >= 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Returning width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Handling exceptions of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Returning the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Handling exceptions for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Returning the x corrdinate of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Handling exceptions of x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Returnung the y coordinate of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returning the area of the rectangle
        """
        return self.height * self.width

    def display(self):
        """
        Printing in stdout the rectangle
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
