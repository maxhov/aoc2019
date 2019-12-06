#!/usr/local/bin/python3

import unittest
from day4 import is_valid_password


class TestStringMethods(unittest.TestCase):

    def test_223450_is_not_valid_password(self):
        p = 223450
        outcome = is_valid_password(p)
        self.assertFalse(outcome)

    def test_123789_is_not_valid_password(self):
        p = 123789
        outcome = is_valid_password(p)
        self.assertFalse(outcome)

    def test_111111_is_not_valid_password(self):
        p = 111111
        outcome = is_valid_password(p)
        self.assertFalse(outcome)

    def test_112233_is_valid_password(self):
        p = 112233
        outcome = is_valid_password(p)
        self.assertTrue(outcome)

    def test_123444_is_not_valid_password(self):
        p = 123444
        outcome = is_valid_password(p)
        self.assertFalse(outcome)

    def test_111122_is_valid_password(self):
        p = 111122
        outcome = is_valid_password(p)
        self.assertTrue(outcome)

    def test_344455_is_valid_password(self):
        p = 344455
        outcome = is_valid_password(p)
        self.assertTrue(outcome)


if __name__ == '__main__':
    unittest.main()
