#!/usr/bin/python3
'''Module for rectangle class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a rectangle'''
    def __init__(self, size):
        '''Constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method for area of square'''
        return self.__size ** 2
