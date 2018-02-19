#!/usr/bin/python

from Emp import Employee

emp=Employee()

print "Calling emp.displayEmployee "
emp.displayEmployee("Rahul",5000)
print "\n"

print "Calling emp.getName "
print "My name is: ",emp.getName(),"\n"

print "Calling emp.displayEmployee "
emp.displayEmployee("Raj",10000)
print "\n"

print "Calling emp.getName "
print "My name is: ",emp.getName(),"\n"

print "Calling emp.displayCount "
emp.displayCount();
print "\n"

print "Calling emp.setName "
emp.setName("Mohit")
print "\n"

print "Calling emp.getName "
print "My name is: ",emp.getName(),"\n"

'''nt "emp.__doc__:",emp.__doc__
#print "emp.__name__:",emp.__name__
print "emp.__module__:",emp.__module__
#print "emp.__base__:",emp.__base__
print "emp.__dict__:",emp.__dict__'''


