#!/usr/bin/python


###raise
def number(num):
	if (num < 0):
		raise RuntimeError("Negative number not expected !")
	print "Positive num is ",num

number(20)
number(-15)
