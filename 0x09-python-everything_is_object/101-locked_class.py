#!/usr/bin/python3
"""This defines a locked class"""


class LockedClass:
    """
    only instatiation of an attribute called frist_name allowed
    """

    __slots__ = ["first_name"]
