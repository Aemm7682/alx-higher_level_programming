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

        new_dict = dict()
        for attr in attrs:
            if not isinstance(attr, str):
                '''If any attribute in attrs is not
                a string, return the entire dictionary'''
                return self.__dict__
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
        return new_dict
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
