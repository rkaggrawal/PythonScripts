#!/usr/bin/python

from __future__ import absolute_import
import unittest
from bin.unittest_pytest_framework.employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #Execute once before start of entire test suit
        print 'setUpClass\n'

    @classmethod
    def tearDownClass(cls): #Execute once after end of entire test suit
        print 'tearDownClass'

    def setUp(self): #Execute before each teat case
        print 'setUp'
        self.emp_1 = Employee('Rajat', 'Mathur', 50000)
        self.emp_2 = Employee('Aman', 'Verma', 60000)

    def tearDown(self): #Execute after each test case
        print 'tearDown'

    def test_email(self):
        print 'test_email'
        self.assertEqual(self.emp_1.email, 'Rajat.Mathur@email.com')
        self.assertEqual(self.emp_2.email, 'Aman.Verma@email.com')

        self.emp_1.first = 'Karan'
        self.emp_2.first = 'Priya'

        self.assertEqual(self.emp_1.email, 'Karan.Mathur@email.com')
        self.assertEqual(self.emp_2.email, 'Priya.Verma@email.com')


    def test_fullname(self):
        print 'test_fullname'
        self.assertEqual(self.emp_1.fullname, 'Rajat Mathur')
        self.assertEqual(self.emp_2.fullname, 'Aman Verma')

        self.emp_1.first = 'Karan'
        self.emp_2.first = 'Priya'

        self.assertEqual(self.emp_1.fullname, 'Karan Mathur')
        self.assertEqual(self.emp_2.fullname, 'Priya Verma')



if __name__ == '__main__':

    unittest.main()