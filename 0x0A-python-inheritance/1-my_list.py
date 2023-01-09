#!/usr/bin/python3
"""Thos module inherits from list"""


class MyList(list):
    """This class inherted from list"""
    def print_sorted(self):
        """function that sort unsorted list"""
        print(sorted(self))
