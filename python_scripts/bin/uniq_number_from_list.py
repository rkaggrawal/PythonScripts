#!/usr/bin/python


list1 = [1,18,4,6,5,4,6,1]
print list1

for i in range(len(list1)):
    count=0
    for j in range(len(list1)):
        if(list1[i]==list1[j]):
            count+=1
    else:
        if(count==1):
            print "unique number is: ",list1[i]
