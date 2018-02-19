#!/usr/bin/python


#1
list1 = ['a','b','c']
list2 = list1
print "list1: ",list1
print "list2: ",list2
list2[1]="mod"
print "list1: ",list1
print "list2: ",list2

print "\n"
list1 = ['a','b','c']
list2 = [1,2,3]
print "list1: ",list1
print "list2: ",list2
list2[1]="mod"
print "list1: ",list1
print "list2: ",list2


#It's possible to completely copy shallow list structures with the slice operator without having any of the side effects, which we have described above.
print "\n"
list1 = ['a','b','c','d']
list2 = list1[:]
list2[1] = 'x'
print "list1: ",list1
print "list2: ",list2

#But as soon as a list contains sublists, we have the same difficulty, i.e. just pointers to the sublists.
lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
#If you assign a new value to the 0th Element of one of the two lists, there will be no side effect. Problems arise, if you change one of the elements of the sublist.
lst2[0] = 'c'
lst2[2][1] = 'd'
print(lst1)
print(lst2)

#A solution to the described problems is to use the module "copy". This module provides the method "copy", which allows a complete copy of a arbitrary list, i.e. shallow and other lists.
print "\n"
from copy import deepcopy
lst1 = ['a','b',['ab','ba']]
lst2 = deepcopy(lst1)
lst2[2][1] = "d"
lst2[0] = "c";
print lst1
print lst2
