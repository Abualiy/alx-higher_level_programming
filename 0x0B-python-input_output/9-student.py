#!/usr/bin/python3
"""class Student that defines a student by"""


class Student:
    """class Student that defines a student by"""


    def __init__(self, frist_name, last_name, age):
        self.frist_name = frist_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
