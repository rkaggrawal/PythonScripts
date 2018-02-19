#!/usr/bin/python

num = int(raw_input("Enter a number for iteration\n"))

prev = 0
curr = 1
count = 3
if num <=0:
	print "Please enter positive number"
elif num == 1:
	print "Fibonaci series is:"
	print prev
else:
	print "Fibonaci series is:"
	print prev,",",curr,
	while count <= num:
		prev, curr = curr, prev+curr 
		#nth = prev + curr
		#print ",",nth,
		print ",", curr,
		#prev = curr
		#curr = nth
		count += 1	
