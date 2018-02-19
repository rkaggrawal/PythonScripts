#!/usr/bin/python

from Emp import childEmployee
emp=childEmployee()
emp.displayEmployee("Rahul",5000)
print "\n"
print emp.getName()
print "\n"
emp.displayEmployee("Raj",10000)
print "\n"
print emp.getName()
print "\n"
emp.displayCount()
print "\n"
emp.setName("Mohit")
print "\n"
print emp.getName(),"\n"

'''nt "emp.__doc__:",emp.__doc__
#print "emp.__name__:",emp.__name__
print "emp.__module__:",emp.__module__
#print "emp.__base__:",emp.__base__
print "emp.__dict__:",emp.__dict__'''


