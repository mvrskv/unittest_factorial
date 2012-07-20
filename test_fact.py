'''
Created on 05.07.2012

@author: mrasskazov
'''
import unittest
import fact
from math import factorial


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_negative_number(self):
        '''Negative x'''
        r = fact.fact(-1)
        self.assertEqual(r, factorial(-1))

    def test_positive_number(self):
        '''Positive x'''
        r = fact.fact(10)
        self.assertEqual(r, factorial(10))

    def test_zero(self):
        r=fact.fact(0)
        self.assertEqual(r, factorial(0))

    def test_one(self):
        r=fact.fact(1)
        self.assertEqual(r, factorial(1))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()