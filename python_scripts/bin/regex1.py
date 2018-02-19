#!/usr/bin/python
import re

string = 'cat,dog,Cat,DOG'

print "Org string: ",string
##match
match = re.match(r'dog|cat',string)
if match:
	print "Match found match.group: ",match.group()
else:
	print "Match not found"

##search
match = re.search(r'(?P<first>\w+),(\w+),(.*)',string)
if match:
	print "search found match.group: ",match.group()
	print "search found match.group: ",match.group('first')
	print "search found match.group: ",match.group(2)
	print "search found match.group: ",match.group(3)
else:
	print "search not found"


##multiple match result re.findall
for match in re.findall(r'cat|dog',string,re.I):
	print 'Found "%s"' % match

##multiple match result re.finditer
for match in re.finditer(r'cat|dog',string,re.I):
	s = match.start()
	e = match.end()
	print 'Found "%s at %d:%d"' % (string[s:e],s,e)

##Substitute
print "After substituing cat with tiger: ",re.sub(r'cat|dog',"tiger",string,re.I)
print "After replacing cat with tiger: ",string.replace("cat","tiger")

names = "rahul aggrawal"
print "After removing space: ",re.sub(r'\s+',"",names)

#var = 1020306
#print "After substituing cat with tiger: ",re.sub(r'0','5',var)

