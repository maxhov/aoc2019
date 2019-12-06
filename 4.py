#!/usr/bin/python

import unittest

start = 145852
end = 616942
input = [x for x in range(start, end)]


def has_two_equal_adjacent_digits(number):
    l = [x for x in str(number)]
    n = 1
    for c in range(0, len(l)-1):
        if l[c] == l[c + 1]:
            n += 1
        else:
            if n == 2:
                return True

            n = 1

    return n == 2


def never_decreases(number):
    l = [x for x in str(number)]
    return l == sorted(l)


def is_valid_password(number):
    if has_two_equal_adjacent_digits(number) and never_decreases(number):
        print(number)
        return True

    return False


potential_passwords = map(is_valid_password, input)
valid_passwords = [x for x in potential_passwords if x == True]

print("In this range, there are {} valid passwords").format(
    len(valid_passwords))


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
