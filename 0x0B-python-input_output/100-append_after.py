#!/usr/bin/python3
"""
    function that inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file"""
    text = ""
    with open(filename) as a_file:
        for line in a_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w_file:
        w_file.write(text)
