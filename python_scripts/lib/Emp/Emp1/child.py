#!/usr/bin/python
from employee import Employee

class Child(Employee):
	'child class'
	
	def __init__(self,name,salary=5000):
		print "Callig child class"
		self._name=name
		self.salary=salary
	
	def childMethod(self):
		print "Callig childMethod"	

	'''def displayEmployee(self):
		print "Calling child displayEmployee"
		print "Name: ",self.name
		print "Salary: ",self.salary'''
		
	'''def setName(self,name):
		print "Callig child setName"
		self.name=name'''
