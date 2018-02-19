#!/usr/bin/python

class Employee:
	'Common base class for all employees'
	__empCount = 0
	message = "Employee class message"
	def __init__(self,name,salary=1000):
		Employee.__empCount += 1
		print "Calling class constructor for employee " + str(Employee.__empCount)
		self._name = name
		self.salary = salary

	def displayCount(self):
		print "Calling parent displayCount"
		print "Total Employee: ",Employee.__empCount

	def _displayEmployee(self):
		print "Calling parent displayEmployee"
		print "Name: ",self._name
		print "Salary: ",self.salary

	def setName(self,name):
		print "Calling parent setName"
		self._name = name

	def getName(self):
		#print "Calling parent getName"
		return self._name

class BankAccount:
	def __init__(self):
		message = "BankAccount class message"
		print "Starting balance is 0"
		print "Calling BankAccount class constructor"
		self.balance = 0
	
	def withdraw(self,amount):
		if amount > self.balance:
			raise RuntimeError('Amount greater than available balance.')
		self.balance -= amount
		return self.balance

	def deposit(self,amount):
		self.balance += amount
		return self.balance
