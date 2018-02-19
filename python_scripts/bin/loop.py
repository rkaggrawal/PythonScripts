#!/usr/bin/python

###While loop

count = 0
while (count < 5):
	count+=1	
	if (count == 3):
		continue
		#break
	print "Number is ",count

else:
	print "While loop end"

###Foor loop

fruits = ['apple','orange','mange','papaya']
tot_fruits = len(fruits)
print "Total fruits are"," ",tot_fruits
for fruit in fruits:
	print "Fruit is ",fruit

else:
	print "For loop end"

for i in range(tot_fruits):
	print "Fruit via len is"," ",fruits[i]

else:
	print "For loop end"

