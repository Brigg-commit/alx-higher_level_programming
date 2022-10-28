#!/usr/bin/python3
"""Student module."""


class Student:
    """Define a class called Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student

        Args:
            first_name(str): first name of the student
            last_name(str): last name of a the student
            age(int): age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = first.age

    def to_json(self):
        """Retrieves a dictionary representation of a student"""
        return self.__dict__
