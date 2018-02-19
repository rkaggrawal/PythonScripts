#!/usr/bin/python
import re

print dir(re)
print help(re.match)
print help(re.search)
#string1 = raw_input("Enter a strin\n")
string1 = "home sweet aHome jaipur"

matchObject = re.search(r'(.*?) sweet (.*?) .*',string1,re.M|re.I)

if matchObject:
	print "match found"
	#matchObject.group() and matchObject.group(0) both are same and always returns the fully matched string.
	print "matchObject.group():",matchObject.group()
	print "matchObject.group(0):",matchObject.group(0)
	
	print "matchObject.group(1): %s" %(matchObject.group(1))
	print "matchObject.group(2):",matchObject.group(2)

else:
	print "match not found"


string2 = "my City is very clean"

matchObject = re.search("city",string2,re.M|re.I)
#matchObject = re.search("[cC]ity",string2,re.M)

if matchObject:
	print "match found",",matchObject.group():",matchObject.group()

else:
	print "match not found"


###Search: It matches anywhere in the string
matchObject = re.search(r'sweet',string1)
if matchObject:
	print "match found",",matchObject.group():",matchObject.group()

else:
	print "match not found"

###matchObject: it matches only at the begining of the string. In following example result will be false as "sweet" is not in begining.
matchObject = re.match(r'sweet',string1)
if matchObject:
	print "match found",",matchObject.group():",matchObject.group()

else:
	print "match not found"
### Will ba able to match "home" as it is in begining of the string.
matchObject = re.match(r'home',string1)
if matchObject:
	print "match found",",matchObject.group():",matchObject.group()

else:
	print "match not found"


