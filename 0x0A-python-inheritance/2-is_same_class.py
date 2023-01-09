#!/usr/bin/python33
""" check if object is instance"""


def is_same_class(obj, a_class):
    """Return True if the object is an instance of the
    class otherwise False
    """
    return (type(obj) == a_class)
