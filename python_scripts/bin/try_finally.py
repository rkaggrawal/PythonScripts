#!/usr/bin/python

try:
	fo = open("testfile","r")
    	try:
		fo.write("My test file for exception handling")
	finally:
		print "Closing file"
		fo.close()
except IOError:
	print "Cant find or read", fo.name
