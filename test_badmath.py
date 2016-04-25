import unittest

import badmath

class TestBadMath(unittest.TestCase):
    def test_addition(self):
        self.assertEquals(badmath.addition(1,1), 2)

    def test_multiplication(self):
        self.assertEquals(badmath.multiplication(1,1), 1)
        

