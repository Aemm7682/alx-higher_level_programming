#!/usr/bin/python3
'''define rectangle and get area and primeter'''


class Rectangle:
    """initiate rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """to print thr rectangle in a symbol"""
        printable = ""
        if self.__width == 0 or self.__height == 0:
            return printable
        for i in range(self.__height):
            printable += (str(self.print_symbol) * self.__width)
            if i != (self.__height - 1):
                printable += '\n'
                """ to return the printable again"""
        return printable

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """to remove the instance of the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
