#!/usr/bin/python

list = ['a','b','c','d','e']
tinylist = ['1','2.0']
print type(list)
print "org list"," ",list  #print complete list
print "list[0]"," ",list[0] #print first element of list
print "list[1:3]"," ",list[1:3] #print element starting from 2nd to 3rd
print "list[2:]"," ",list[2:] #print element starting from 2nd

print "\norg tinylist"," ",tinylist  #print complete list
print "tinylist * 2"," ",tinylist * 2 #print list two times

print "\nlist + tinylist"," ",list + tinylist #print concatenated lists
list.extend(tinylist)
print "list.extend(tinylist)"," ",list#extend list

list[0] = 'f'
print "list after modify"," ",list

print "\n"
list = ['a','b','c','d','e']
print "List is ",list

print "Index of c is: ",list.index('c')
list.insert(8,'i')
print "Index of i is: ",list.index('i')
list.insert(3,'z')
list.insert(5,'z')
print "List is ",list
list.remove('z') #Removes the item and Returns nothing
print "List is ",list
print "list.pop(4): ",list.pop(4) #Removes the item and returns the item
print "List is ",list

print "\n"
#There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list
print "before delete item at index 2 is list[2]", list[2]
del list[2]
print "Aftre del list[2] list is ",list
print "after delete item at index 2 is list[2]", list[2]
del list[1:3]
print "Aftre del list[1:3] list is ",list
del list[:] #Delete all elemets of list
print "Aftre del list[:] list is ",list
del list #Delete list completely
print "Aftre del list list is ",list

print "\n"
list = ['a','b','c','d','e']
print "\n\nList is ",list
print "list[2] ",list[2]
print "list[-1] ",list[-1]
print "list[-2]", " ",list[-2]
print "list[-3]", " ",list[-3]
print "list[-5]", " ",list[-5]
print "list[1:]", " ",list[1:]
print "list[:3]", " ",list[:3]
print "list[1:3]", " ",list[1:3]
print "list[-3:-1]", " ",list[-3:-1]

##len function
print "length of list is"," ",len(list)


##list+tinylist
list3 = list+tinylist
print "list3 is: ",list3

##append method
print "list.append(\"f\")"
list.append("f")
print "After append list is"," ",list
print "Index of f is: ",list.index("f")

print "list.append(\"c\")"
list.append("c")
print "After append list is"," ",list

print "Count number of time \"c\" appeared in list using method list.count()"," ",list.count('c')

print "\n"
##Reverse list: Method1
list = [1,2,3,4]
print "Org list: ",list
list.reverse()
print "list.reverse()"," ",list

print "\n"
##Reverse list: Method2
a = [1,2,3]
print "Org list: ",a
a = a[::-1]
print "List after reverse: ",a

print "\n"
##Reverse list: Method3
c = [1,2,3,4]
print "Org list: ",c
i = 0
j = len(c)-1
while i<j:
    c[i], c[j] = c[j], c[i]
    i +=1
    j -=1
else:
    print "Reversed list is: ",c


print "\n"
##Sort list without using sort method
a = [4,1,5,2]
print "Org list: ", a
for i in range (len(a)):
    for j in range(len(a)):
        print a[i],a[j]
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

else:
    print "Sorted list is: ", a


##Sort list without using sort method - Bubble Sort
print "\nBubble Sort"
a = [4,1,5,2]
print "Org list: ", a
for i in range (len(a)):
    for j in range(len(a)-i-1):
        # print a[j],a[j]
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            # print a
    # print "fineshed inner for loop"
else:
    print "Sorted list is: ", a