#!/usr/bin/python

try:
	fo = open("testfile","w")
    	fo.write("My test file")
except IOError:
	print "Error: cant find or read",fo.name
else:
	print "Written content in",fo.name
	fo.close()



try:
	fo = open("testfile","r") #Opening file in read mode and trying to Write
    	fo.write("My test file")
except IOError:
	print "Error: cant find or write",fo.name
else:
	print "Written content in",fo.name
	fo.close()

