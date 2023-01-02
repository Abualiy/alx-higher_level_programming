#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            if width > 0:
                self.__width = value
        except TypeError:
            print("width must be an intger")
        except ValueError:
            print("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if height > 0:
                self.__height = value
        except TypeError:
            print("height must be an integer")
        except ValueError:
            print("height must be >= 0")

    def area(self):
        return (width * height)

    def perimeter(slef):
        if width == 0 or height == 0:
            Rectangle.perimeter(0)
        else:
            return ((2 * height) + (2 * width))
