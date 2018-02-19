#!/usr/bin/python

class Employee:
    raise_amount = 1.02
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

    def __repr__(self):
        return self.fullname()

    def __str__(self):
        return self.email

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Cory', 'Duggins', 10000)
emp_2 = Employee('Savitlana', 'Harms', 20000)

print emp_1
print repr(emp_1)
print str(emp_1)

print '\n'
print emp_1.__repr__()
print emp_1.__str__()

print '\n'

print(2+3)
print('b'+'c')

print int.__add__(2, 3)
print str.__add__('b', 'c')
print (emp_1 + emp_2)

print len('python')
print len(emp_1)