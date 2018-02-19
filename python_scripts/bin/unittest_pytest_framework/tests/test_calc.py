#!/usr/bin/python

import unittest
import bin.unittest_pytest_framework.calc
import pytest

class TestCalc(unittest.TestCase):

    def test_add(self):
        # result = calc.add(10, 5)
        self.assertEqual(bin.unittest_pytest_framework.calc.add(10, 5), 15)
        self.assertEqual(bin.unittest_pytest_framework.calc.add(-1, 1), 0)
        self.assertEqual(bin.unittest_pytest_framework.calc.add(-1, -1), -2)

    def test_subtract(self):
        # result = calc.add(10, 5)
        self.assertEqual(bin.unittest_pytest_framework.calc.subtract(10, 5), 5)
        self.assertEqual(bin.unittest_pytest_framework.calc.subtract(-1, 1), -2)
        self.assertEqual(bin.unittest_pytest_framework.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        # result = calc.add(10, 5)
        self.assertEqual(bin.unittest_pytest_framework.calc.multiply(10, 5), 50)
        self.assertEqual(bin.unittest_pytest_framework.calc.multiply(-1, 1), -1)
        self.assertEqual(bin.unittest_pytest_framework.calc.multiply(-1, -1), 1)

    def test_divide(self):
        # result = calc.add(10, 5)
        self.assertEqual(bin.unittest_pytest_framework.calc.divide(10, 5), 2)
        self.assertEqual(bin.unittest_pytest_framework.calc.divide(-1, 1), -1)
        self.assertEqual(bin.unittest_pytest_framework.calc.divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            bin.unittest_pytest_framework.calc.divide(10, 0)

class TestCalcPy(object):

    def test_py_add(self):
        assert bin.unittest_pytest_framework.calc.add(10, 5) == 15
        # self.assertEqual(calc.add(-1, 1), 0)
        # self.assertEqual(calc.add(-1, -1), -2)

    def test_zero_division_error(self):
        with pytest.raises(ValueError):
            bin.unittest_pytest_framework.calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()

#unittest cases run from cli
## python test_calc.py -v [Run entire module]
## python test_calc.py TestCalc.test_add [Run one test]

#pytest cases run from cli
## py.test test_calc.py -v