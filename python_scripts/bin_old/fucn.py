#!/usr/bin/python

def printName(age,name):
	print "Name is:",name
	print "Age is:",age

printName(name="Rahul",age=30)
#printName("Rahul",30)

def printInfo(arg1,*variables):
	print "Output is:"
	print arg1
	for var in variables:
		print var

printInfo(10,20)
printInfo('Raj',30,40,50)

def printme1 (str):
		print str
		return	

printme1("I am employee of Symantec!!")
printme1("I am working in Veritas!!")

def printme2 (*str):
		for var in str: 
			print var

printme2("I am employee of Symantec!!","I am working in Veritas!!")

