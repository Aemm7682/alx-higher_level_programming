#!/usr/bin/python3
"""new module for square from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return square info"""
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """size = height and width"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update_fun(self, id=None, size=None, x=None, y=None):
        """auxiliary function to update"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """to update the value"""
        if args:
            self.update_fun(*args)
        elif kwargs:
            self.update_fun(**kwargs)
