#!/usr/bin/python3
"""
    function that writes a string to a text file (UTF8)
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    """unction that writes a string to a text file"""
    with open(filename, mode="w", encoding="utf-8") as a_file:
        a_file.write(text)
