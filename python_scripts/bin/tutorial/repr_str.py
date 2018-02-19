#!/usr/bin/python
import datetime

class Employee(object):
    raise_amount = 1.05
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #comment __repr__ and __str__ code and than run it to see difference
    def __repr__(self):
        return "I am in repr"
        # return 'I am {} {} and I earn {}'.format(self.first, self.last, self.pay)

    def __str__(self):
        return "I am in str"

    #Operator overloading
    def __add__(other1, other2):
        return other1.pay + other2.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Anderson', 4000)
emp_2 = Employee('Brett', 'Lee', 7000)
print emp_1

print("\n")
print(repr(emp_1))
print(emp_1.__repr__())

print("\n")
print(str(emp_1))
print(emp_1.__str__())

print("\n")
print(1+2)
print(int.__add__(1, 2))

print "\n"
print(len('test'))

#Operator overloading
print "\n"
print(emp_1 + emp_2)

print 'len is {}'.format(len(emp_1))