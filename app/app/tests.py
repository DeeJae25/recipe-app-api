"""
sample tests
"""

from django.test import SimpleTestCase
from . import calc


class CalcTests(SimpleTestCase):
    """ test the calc module"""

    def test_add_numbers(self):
        """ start your def name with test as prefix"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(5, 15)
        self.assertEqual(res, 10)
