#!/usr/bin/python

for i in range(2,10,4):
	print i

range(5)
print type(range(5))
print range(1,6)

s = "this is my string"
result = str ()
for i in range(len(s)-1,-1,-1):
    result += s[i]
else:
    print result

words =  s.split(' ') #This will create list of words
print words
revstr = str()
for word in range(len(words)-1,-1,-1):
    revstr += words[word] + " "
else:
    print revstr

newstr = str()
for word in words:
    #str = words[word]
    for i in range(len(word)-1,-1,-1):
	newstr += word[i]
    else:
	newstr += " "
else:
    print newstr

