#!/usr/bin/python


##Replace '0' with '5'
##Method1
print "Method1"
var = 1020306
print type(var)
print var

#list = list(str(var))
list = map(int,str(var))
var1 = str()

for i in range (len(list)):
    if (list[i] == 0):
        var1 = var1 + '5'
    else:
        var1 = var1 + str(list[i])
else:
    print int(var1)


##Method2
##str(var), converts integer into string
##To convert str into int use: int(x [,base]) - Converts x to an integer. base specifies the base if x is a string.
print "Method2"
print str(var).replace('0','5')
print str(var).replace('0','5',2)


##Convert str into int
print "\nConvert str into int"
str1 = "12345"
print type(str1)
print str1
int1 = int(str1)
print type(int1)
print int1


##Convert int into string
print "\nConvert int into string"
int2 = 12345
print type(int2)
print int2
str2 = str(int2)
print type(str2)
print str2

