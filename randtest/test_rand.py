"""
Random number tests.  One always succeeds and one fails part of the time.
"""
import unittest

import random

class TestRand(unittest.TestCase):
    """ Random Number Generator Test """
    def __init__(self, *args, **kwargs):
        """ Initialize the RNG """
        super().__init__(*args, **kwargs)

        random.seed()

    def test_success(self):
        """ Always successful """
        value = random.random()
        self.assertGreaterEqual(xvalue, 0.0)
        self.assertLessEqual(value, 1.0)

    def test_50(self):
        """ Successful 50% of the time """
        value = random.random()
        self.assertLess(value, 0.5)

if __name__ == '__main__':
    unittest.main()
