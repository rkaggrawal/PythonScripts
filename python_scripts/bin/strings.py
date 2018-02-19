#!/usr/bin/python

string1 = 'AbcdE'
print "Org string1 is"," ",string1
print id(string1)
#string1[0]='B' #strings in python are immutable.

print list(string1)
#print "".join(list)
for x in string1:
    print x
print "string1[1]"," ",string1[1]

lenstr = len(string1)
print "String length is ",lenstr
lenstr -=1 
revstr=""
while (lenstr >=0):
    revstr = revstr+string1[lenstr]
    lenstr -=1
print "Reverse string is: ",revstr

swapc = revstr.swapcase()
print "After swapcase string is: ",swapc

string2 = string1 + '123'
print "string2 is"," ",string2

string1 = string1.upper();
print "UPPER string is"," ",string1

string1 = string1.lower();
print "lower string is"," ",string1

tuple = ("a","b","c","d")
sep = "--"
mod_tuple = "--".join(tuple)
print "org tuple is: ",tuple
print "sep.join(tuple)"," ","--".join(tuple)

#2 is for how many "--" you want to split.In this case only first 2 "--" will be split rest will remain.
print "mod_tuple.split('--',1)"," ",mod_tuple.split('--',1)
print "mod_tuple.split('--',2)"," ",sep.join(tuple).split('--',2)

##How to split from right side
str = "192.168.31.92"
print str.rsplit('.', 1) #1 is for how many occurence fron right side to split.
print str.rsplit('.', 2)
print str[-4:]
print str.replace('9', '7')
#===
str = "do do do do?"
print "str.replace(\"do\",\"are\",3)"," ",str.replace("do","are",3)

nostr = 'This is my \t\tnormal string'
rawstr = r'This is my \t\t raw string'

print "nostr: ",nostr
print "rawstr: ",rawstr


print "\n\n"
print dir(str)