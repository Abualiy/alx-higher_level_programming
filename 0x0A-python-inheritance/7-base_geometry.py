#!/usr/bin/python3
<<<<<<< HEAD
"""Define a base geometry class"""


class BaseGeometry:
    """this class represent a base geometry"""

    def area(self):
        """
=======
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """this class represents a base geometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
>>>>>>> 00503bcd96c58596500116ddd97fbf725fc4c8c8
