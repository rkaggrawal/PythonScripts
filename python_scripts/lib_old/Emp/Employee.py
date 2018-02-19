#!/usr/bin/python

class Employee:
	'Common base class for all employees'
	def __init__(self,name="",salary=0,empCount=0):
		self.name=name
		self.salary=salary
		self.empCount =empCount	
	
	def displayCount(self):
		print "Calling Parent class method displayCount()","\n","Total Employee:",self.empCount	
	
	def displayEmployee(self,a,b):
		self.name=a
		self.salary=b
		self.empCount+=1	
		print "Calling Parent class method displayEmployee()","\n","Name: ",self.name, ", salary: ",self.salary
	
	def setName(self,a):
		print "Calling Parent class method setName()"
		self.name=a

	def getName(self):
		print "Calling Parent class method getName()"
		return self.name

