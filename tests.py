#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The tests."""

from unittest import TestCase
from fzbz import FizzBuzz

class FzBzTest(TestCase):
    """Fizz Buzz Test."""

    def setUp(self):
        """Setup."""
        self.obj = FizzBuzz()

    def test_num(self):
        """The return value should be based of FizzBuzz."""
        for n in range(100):
            with self.subTest(n=n):
                ret = self.obj()
                exp = "FizzBuzz" if n % 3 == 0 and n % 5 == 0 else \
                    "Fizz" if n % 3 == 0 and n % 5 != 0 else \
                    "Buzz" if n % 3 != 0 and n % 5 == 0 else \
                    str(n)
                self.assertEqual(ret, exp)
