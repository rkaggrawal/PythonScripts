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

print Employee.num_of_emps
emp_1 = Employee('Cory', 'Duggins', 10000)
emp_2 = Employee('Savitlana', 'Harms', 20000)
print Employee.num_of_emps

print emp_1.__dict__
print Employee.__dict__

print Employee.raise_amount
print emp_1.raise_amount
print emp_2.raise_amount

Employee.raise_amount = 1.05
print Employee.raise_amount
print emp_1.raise_amount
print emp_2.raise_amount

emp_1.raise_amount = 1.06
print Employee.raise_amount
print emp_1.raise_amount
print emp_2.raise_amount
print emp_1.__dict__




# print emp_1.fullname()
# print Employee.fullname(emp_1)