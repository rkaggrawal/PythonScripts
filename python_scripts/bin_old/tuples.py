#!/usr/bin/python

tuples = ('abcd','1234','ABCD','SYMC')
tinytuples = ('Perl','Pyhton')
print tuples
print tuples[0]
print tuples[1:3]
print tuples[1:]
print tinytuples * 2
print tuples+tinytuples

tupLength = len(tuples)
print "Tuple length is: ",tupLength
#del tuples
#print tuples
