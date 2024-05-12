#!/usr/bin/python3
"""new class inherant from base"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""


    def __init__(self, width, height, x = 0, y = 0, id = None):
        """constractor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        self.__width = width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        self.__height = height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        self.__x = x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        self.__y = y

    @y.setter
    def y(self, value):
        self.__y = value
