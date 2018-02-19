#!/usr/bin/python

#How will you check in a string that all characters are digits?
##isdigit()
#Returns true if string contains only digits and false otherwise.
print "isdigit()"
str = "1245"
print str.isdigit()
str = str+"abc"
print str.isdigit()

#How will you check in a string that all characters are alphanumeric?
#isalnum() . Returns true if string has at least 1 character/int and all characters/int are alphanumeric and false otherwise.
print "\nisalnum()"
str = ""
print str.isalnum() #returns False as it need at leats one char/int

str = "1234abcd" #returns True
print str.isalnum()

str = "1234#abcd"
print str.isalnum() #returns False as it contains non alphanumeric character '#'

#How will you check in a string that all characters are in lowercase?
#islower()
print "\nislower()"
str = "abcA"
print str.islower()
str = "abc"
print str.islower()

#How will you check in a string that all characters are in upercase?
#isupper()
print "\nisupper()"
str = "abcA"
print str.isupper()
str = "AB"
print str.isupper()
