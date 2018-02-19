#!/usr/bin/python

tuple = ('a','b','c','d','e')
tinytuple = ('1','2.0')

print "org tuple"," ",tuple  #print complete tuple
print "tuple[0]"," ",tuple[0] #print first element of tuple
print "tuple[1:3]"," ",tuple[1:3] #print element starting from 2nd to 3rd
print "tuple[2:]"," ",tuple[2:] #print element starting from 2nd

print "\norg tinytuple"," ",tinytuple  #print complete tuple
print "tinytuple * 2"," ",tinytuple * 2 #print tuple two times

print "tuple + tinytuple"," ",tuple + tinytuple #print concatenated tuples 

print tuple
tuple[0] = 'f'
