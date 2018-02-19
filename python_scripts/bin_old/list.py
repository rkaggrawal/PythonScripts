#!/usr/bin/python
#import list
list = ['abcd','1234','ABCD','SYMC']
tinylist = ['Perl','Pyhton']
print list
print list[0]
print list[1:3]
print list[1:]
print tinylist * 2
print list+tinylist
#Modify list
list [3]='Rahul'
print "After modification list is: "
print list
list.append('Raj')
print list
list.reverse()
print list
list.remove('ABCD')
print list
item = list.pop()
print list
print item
list.insert(6,'Iamsix')
list.insert(5,'ABCD')
list.insert(2,'ABCD')
print list
count = list.count('ABCD')

print "ABCD counbt is:",count
