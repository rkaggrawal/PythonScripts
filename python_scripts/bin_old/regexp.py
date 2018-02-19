#!/usr/bin/python

import re

input=raw_input("Enter you name:")

m=re.search("(?i)Rahul",input)

if m:
	print "\nMatched !!"
	mos=re.sub("(?i)Rahul","Raj",input)
	print "Updated string: ",mos
else:
	print "\nSORRY-No match found !!"	
