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
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.valid_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.valid_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.valid_int("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.valid_int("y", value)
        self.__y = value

    def valid_int(self, name, value, eq=True):
        """method to vaildate the value is integar"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ method to find the area of rectangle"""
        return self.height * self.width

    def display(self):
        """to display Rectangle with hash #"""
        disp = ('\n' * self.y) + \
            (" " * self.x + '#' * self.width + '\n') * self.height
        print(disp, end="")

    def __str__(self):
        """print rectangle information in string format"""
        return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__, self.id, self.x, self.y,
                self.width, self.height)

    def update_fun(self, id=None, width=None, height=None, x=None, y=None):
        """ internal method to help update functiom"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args):
        """to update value by using *arg"""
        if args:
            self.update_fun(*args)
