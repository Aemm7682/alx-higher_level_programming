#!/usr/bin/python3
"""new class inherant from base"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constractor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value : int):
        self.__width = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value : int):
        self.__height = value

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, value : int):
        self.__x = value

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, value : int):
        self.__y = value
