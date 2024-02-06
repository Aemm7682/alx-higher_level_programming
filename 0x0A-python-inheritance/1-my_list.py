#!/usr/bin/python3
'''MyList that inherits from list'''


class MyList(list):
    '''Mylist class'''
    def print_sorted(self):
        ''' method to print sorted list'''
        print(sorted(self))
