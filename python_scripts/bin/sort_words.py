#!/usr/bin/python

try:
	my_str = raw_input("Enter a line\n")
except EOFError:
	print "ERROR: You should enter a string !"

else:
	words = my_str.split()
	#Sort the list
	words.sort()
	#Print sorted words
	for word in words:
		print word,"\n"
	
