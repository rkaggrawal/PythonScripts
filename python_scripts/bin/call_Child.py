#!/usr/bin/python

from Emp.Emp1 import Child

emp1 = Child("Suresh")
emp1.childMethod()
emp1._displayEmployee()
emp1.setName("Raman")
print "emp name is: ",emp1.getName()
emp1.displayCount()
