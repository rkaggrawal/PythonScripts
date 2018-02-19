#!/usr/bin/python
import datetime

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday():
        day_num = datetime.datetime.today().weekday()
        print datetime.datetime.today()
        print datetime.datetime.now()
        if day_num > 4:
            return False
        return True



emp_1 = Employee('Cory', 'Duggins', 10000)
emp_2 = Employee('Savitlana', 'Harms', 20000)

Employee.set_raise_amt(1.07)
print Employee.raise_amount
print emp_1.raise_amount
print emp_2.raise_amount

emp_str_3 = "Steve-Smith-40000"
emp_3 = Employee.from_string(emp_str_3)
print emp_3.email
print emp_3.pay

print Employee.is_workday()


# print emp_1.fullname()
# print Employee.fullname(emp_1)