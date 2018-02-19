#!/usr/bin/python
#string = "Hello, Python!"
#lower()
#print string

num = raw_input("\n\nEnter number-\n")
print "You entered: ", num
import time;

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime

print "\nEnter your name:\n"
name = raw_input()
print "Hello",name
