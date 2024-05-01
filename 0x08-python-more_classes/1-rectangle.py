#!/usr/bin/python3
"""
empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    rectangle class"""
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object with optional width and height.

        Parameters:
        width (int): The width of the rectangle. Default is 0.
        height (int): The height of the rectangle. Default is 0.

        Returns:
        None
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")

        @property
        def height(self):
            return self.__height

        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
