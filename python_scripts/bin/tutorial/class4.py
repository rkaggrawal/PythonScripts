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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.insertLast(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print emp.fullname()


emp_1 = Employee('Cory', 'Duggins', 10000)
emp_2 = Developer('Savitlana', 'Harms', 10000, 'Python')

emp_1.apply_raise()
emp_2.apply_raise()

print help(Developer)
print emp_1.email
print emp_1.pay
print emp_2.email
print emp_2.pay
print emp_2.prog_lang

mgr_1 = Manager('Sue', 'Smitj', 15000, [emp_1])
print mgr_1.email
mgr_1.print_emp()

print '\n'
mgr_1.add_emp(emp_2)
mgr_1.print_emp()

print '\n'
mgr_1.remove_emp(emp_1)
mgr_1.print_emp()

print '\n'
print isinstance(mgr_1, Manager)
print isinstance(mgr_1, Employee)
print isinstance(mgr_1, Developer)

print '\n'
print issubclass(Manager, Employee)
print issubclass(Manager, Developer)
print issubclass(Developer, Employee)



