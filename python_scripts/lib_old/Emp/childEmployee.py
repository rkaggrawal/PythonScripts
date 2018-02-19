#!/usr/bin/python

from Employee import Employee

class childEmployee(Employee):
	def __init__(self,name="",salary=0,empCount=0):
		self.name=name
		self.salary=salary
		self.empCount=empCount

	def displayCount(self):
		print "Calling child class method displayCount()","\n","Total Employee are:",self.empCount	
		Employee.displayCount(self)
	
	def displayEmployee(self,a,b):
		self.name=a
		self.salary=b
		self.empCount+=1
		if self.empCount==1:
			 Employee.displayEmployee(self,self.name,self.salary)
		else:	
			print "Calling Child class method displayEmployee()","\n","Name: ",self.name, ", salary: ",self.salary	

	'''def setName(self,a):
		self.name=a

	def getName(self):
		return self.name'''

