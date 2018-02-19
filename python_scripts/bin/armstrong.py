#!/usr/bin/python

inputnum = int(raw_input("Enter a number\n"))

num1 = inputnum
outnum = 0
flag =1
while(flag == 1):
	if (num1/10 > 0):
		div = num1/10
		mod = num1%10
		outnum += (mod * mod * mod)
		num1 = div
	else:
		outnum += (num1 * num1 *num1)
		flag = 0		
else:
	if ( outnum == inputnum):
                print inputnum,"is a armstrong number"
        else:
                print inputnum,"is not a armstrong number"

