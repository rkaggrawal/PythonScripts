#!/usr/bin/python

var = raw_input("Enter anumber\n")
#var = var.replace('\n',"")
#var = var.strip('\n')
print "Number is",":",var

#var = 5

if ( var <= 100 ):
	print "entered number is below 100"
elif ( var <= 200 ):
	print "entered number is between 101 and 200"
else:
	print "entered number is above 200"

print "Good Bye !"
