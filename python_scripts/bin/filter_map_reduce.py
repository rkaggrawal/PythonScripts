#!/usr/bin/python

#filter is used to check the test of value and returns if its True. In our case only those values will be returned which are divisible by 5
#The function filter(function, list) offers an elegant way to filter out all the elements of a list, for which the function function returns True. 
#The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True or False. This function will be applied to every element of the list l. Only if f returns True will the element of the list be included in the result list.

#If sequence is a str, unicode or tuple, the result will be of the same type; otherwise, it is always a list
print "filter(function, sequence)"
def f(x):
    return x%5 ==0
    #return x+x
print filter(f, range(1,26)) #Will return list
print filter(f, (5,10,24,23)) #Will return tuple

#map funtion always returns the list of result after performing operation
#map() applies the function func to all the elements of the sequence seq. It returns a new list with the elements changed by func.
print "\n"+"map(function, sequence, [sequence)"
def cube(x):
    return x**3
print map(cube, range(1,11))

def double(x):
    return x*2
print map(double, "rahul") #Will return list, map always returns list even if seq is str or tuple

seq = range(8)
# seq1 = range(7)
def add(x,y):
    return x+y
print map(add,seq,seq) #Will pass 1 element from each seq


#reduce(function, sequence) returns a single value constructed by calling the binary function on the first two items of the sequence, then on the result and the next item, and so on. For example, to compute the sum of the numbers 1 through 10
#In reduce function like add should take two arguments else call via reduce will fail.
#If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
#At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
#In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
#The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
#Continue like this until just one element is left and return this element as the result of reduce()
print "\n"+"reduce(function, sequence)"
def add(x,y):
    return x+y
print reduce(add, range(1,11))

def square(x,y):
    return x*y

print reduce(square, range(1,5))

f = lambda a,b: a if (a > b) else b
print "Maximum value from list is", reduce(f, [15,10,60,45,105,100])

def min(x, y):
    if (x < y):
        return x
    else:
        return y
print "Minimum value from list", reduce(min, [15,10,60,45,105,100])