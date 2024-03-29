#!/usr/bin/python3
'''make a student class'''


class Student:
    '''intialize the student class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for attr in attrs:
            if not isinstance(attr, str):
                '''If any attribute in attrs is not
                a string, return the entire dictionary'''
                return self.__dict__
            if attr in self.__dict__:
                new_dict[attr] = self.__dict__[attr]
        sorted_dict = {key: new_dict[key] for key in sorted(new_dict)}
        return sorted_dict
