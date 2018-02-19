#!/usr/bin/python

count=0

while (count<=3):
	count+=1
	if count==3:
		continue
	print "Count is:",count
else:
	print "While loop exits!!"
names = ['Rajesh','Rahul','Ram']
for name in names:
	print "Name is:",name
for index in range (len(names)):
	print index,"Name is:",names[index]
else:
	print "For loop exits!!"

print "Progam ends here!!"
	
