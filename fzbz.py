#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test fixture that is written in python."""

class FizzBuzz(object):
    """FizzBuzz."""

    def __init__(self, init: int=0):
        """Init."""
        self.__num = init

    def __call__(self) -> str:
        """Call."""
        ret = []
        if self.__num % 3 == 0:
            ret.append("Fizz")
        if self.__num % 5 == 0:
            ret.append("Buzz")
        if not ret:
            ret.append(str(self.__num))
        self.__num += 1
        return ("").join(ret)
