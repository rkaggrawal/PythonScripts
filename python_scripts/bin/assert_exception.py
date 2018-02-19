#!/usr/bin/python


###assertion
def number(num):
	assert (num>=0),"Negative number not expected !"
	print "Positive num is ",num

number(10)
#number(-5)


def number(num):
	if (num < 0):
		raise RuntimeError("Negative number not expected !")
	print "Positive num is ",num

number(20)
number(-15)
