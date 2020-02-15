#!/usr/bin/python
import re

print dir(re)
print help(re.match)
print help(re.search)
print help(re.findall)
print help(re.sub)
print help(re.subn)
#string1 = raw_input("Enter a strin\n")
string1 = "home  is sweet aHome pink sweet1 jaipur"

matchObject = re.search(r'(.*?) sweet (.*?) (.*)',string1,re.M|re.I)

if matchObject:
	print "match found"
	#matchObject.group() and matchObject.group(0) both are same and always returns the fully matched string.
	print "matchObject.group():",matchObject.group()
	print "matchObject.group(0):",matchObject.group(0)
	
	print "matchObject.group(1): {}".format(matchObject.group(1))
	print "matchObject.group(2):",matchObject.group(2)
	print "matchObject.group(3):",matchObject.group(3)

else:
	print "match not found"


string2 = "my City is very clean"

matchObject = re.search("city",string2,re.M|re.I)
#matchObject = re.search("[cC]ity",string2,re.M)

if matchObject:
	print "\nmatch found",",matchObject.group():",matchObject.group()

else:
	print "match not found"

rep_string = re.sub('City', 'town', string2, re.M|re.I)
print("After sub, string is: {}".format(rep_string))

###Search: It matches anywhere in the string
matchObject = re.search(r'sweet',string1)
if matchObject:
	print "match found",",matchObject.group():",matchObject.group()

else:
	print "match not found"

###matchObject: it matches only at the begining of the string. In following example result will be false as "sweet" is not in begining.
matchObject = re.match(r'sweet',string1)
if matchObject:
	print "\nmatch found",",matchObject.group():",matchObject.group()

else:
	print "\nmatch not found"
### Will ba able to match "home" as it is in begining of the string.
matchObject = re.match(r'home',string1)
if matchObject:
	print "match found",",matchObject.group():",matchObject.group()

else:
	print "match not found"


##re.findall examples - find words starting with a or e
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#find all the words starting with 'a' or 'e'
list = re.findall("[ae]\w+", text)
# Print result.
print(list)

ip = "010.08.094.196"
string = re.sub('[0]+', '', ip)
print(string)