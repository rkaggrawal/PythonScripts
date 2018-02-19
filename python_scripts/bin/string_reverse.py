#!/usr/bin/python

for i in range (2,10,4):
	print i

s = "this is my string"

#Method1
print ''.join(reversed(s))

#Method2
print "Org string: ",s
result = str ()
for i in range(len(s)-1,-1,-1):
    result += s[i]
else:
    print "Reversed string: ",result

#Method3
words =  s.split(' ')
print words
revstr = str()
for word in range(len(words)-1,-1,-1):
    revstr += words[word] + " "
else:
    print "String after word reverse: ",revstr

#Method4
revstr1 = ""
for word in words:
    for i in range(len(word)-1,-1,-1):
        revstr1 += word[i]
    else:
        revstr1 += " "
else:
    print "String after reverse is : ",revstr1
        
#print type(revstr1)

#Method5
revstr2 = ""
for i in range(len(words)-1, -1, -1):
    #word = words[i]
    for j in range(len(words[i])-1, -1, -1):
        revstr2 += words[i][j]
    else:
        revstr2 += " "
else:
    print "String after reverse is : ",revstr2
