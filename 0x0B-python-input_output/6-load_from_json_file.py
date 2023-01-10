#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """ function that creates an Object """
    with open(filename) as a_file:
        return json.load(a_file)
