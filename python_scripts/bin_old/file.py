#!/usr/bin/python
import os

fo = open("foo.txt","w+")
fo.write( "Python is a great language.\nYeah its great!!\n");
print "Name of the file: ", fo.name
print "Closed or not: ", fo.closed
print "Opening mode: ", fo.mode
print "Softspace flag: ", fo.softspace
fo.close ()

fo = open("foo.txt","r")
str = fo.read();
print "Read string is :", str
fo.close ()

os.rename("foo.txt","foo1.txt")
os.remove("foo1.txt")
