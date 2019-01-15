#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test fixture that is written in python."""

class FizzBuzz(object):
    """FizzBuzz."""

    def __init__(self, init: int=0):
        """Init."""
        self.__num = init

    def __call__(self):
        """Call."""
        ret_str = ""
        if self.__num % 3 == 0:
            ret_str += "Fizz"
        if self.__num % 5 == 0:
            ret_str += "Buzz"
        if not ret_str:
            ret_str += str(self.__num)
        self.__num += 1
