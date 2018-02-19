#!/usr/bin/python


#from Emp import Employee,BankAccount
#from Emp.Emp1 import BankAccount

# from Emp.Emp1 import *
# print Employee.message
# print dir (BankAccount)
# emp1 = Employee("employee1",5000)
# print dir(emp1)
# print "Employee count is: ", emp1._Employee__empCount
# print "Employee name is: ", emp1._name
# print "Employee salary is: ", emp1.salary
#
# print "\n"
# emp2 = Employee("employee2")
# print "Employee count is: ", emp1._Employee__empCount
# print "Employee name is: ", emp2._name
# print "Employee salary is: ", emp2.salary



import Emp.Emp1
print Emp.Emp1.Employee.message
print dir (Emp.Emp1.BankAccount)
emp1 = Emp.Emp1.Employee("employee1",5000)
print dir(emp1)
print "Employee count is: ", emp1._Employee__empCount
print "Employee name is: ", emp1._name
print "Employee salary is: ", emp1.salary



emp1._displayEmployee()
emp1.displayCount()
emp1.setName("Raj")
#print "name is: ",emp1.getName()
emp1._displayEmployee()

'''
emp2.displayEmployee()
'''

from Emp.Emp1 import BankAccount
a = BankAccount()
print "balance of employee \"a\" after deposit(700): ",a.deposit(700)
print "balance of employee \"a\" after withdraw(500): ",a.withdraw(500)
print "balance of employee \"a\" after deposit(600): ",a.deposit(600)
print "balance of employee \"a\" after withdraw(1000): ",a.withdraw(1000)