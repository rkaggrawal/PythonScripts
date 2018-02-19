#!/usr/lib/python

# Using for loop
print "Using for loop"
squares = []
for x in range(10):
    squares.append(x**2)
else:
    print squares
   
# Using list comprehension
print r'Using list comprehension, squares = [x**2 for x in range(10)]'
squares = [x**2 for x in range(10)]
print squares

##Example 2
string = 'abacada'
string = [x for x in string if x!='a' and x!='b']
print string
print "".join(string)

##Example 3
list = [1,2,3,4,1]
print "org list is: ", list
list = [10 if x==1 else x for x in list]
print list


#Nested list comprehension

nestList = [(i,j) for i in range(3) for j in range(i+1)]
print "Nested list is: ", nestList

nestList = [(i,j) for i in range(1,3) for j in range(i+1) if i==j]
print "Nested list is: ", nestList

nestList = [(i,j) if i==j else 'Not Equal' for i in range(1,3) for j in range(i+1)]
print "Nested list is: ", nestList


list1 = ['a','b','c']
list2 = list1
list3 = list1[:]
print id (list1)
print id (list2)
print id (list3)

string1 = 'abacada'
#string1['0'] = 'z' #Strings are immutable. You can not change string data.


print "list1: ",list1
print "list2: ",list2
print "list3: ",list3

list1.remove('a')
print "list1: ",list1
print "list2: ",list2
print "list3: ",list3
