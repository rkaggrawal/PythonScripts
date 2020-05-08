#!/usr/bin/python

##Nested function
def func1(msg):
    '''this is my first func1'''
        
    def func2():
	    '''this is my second func2'''
	    print msg

    func2()

func1("Hello")
'''
When top function(enclose) returns inner function(nested) is called as Closure in python.
When Do We Have a Closure?
As seen from the below example, we have a closure in Python when a nested function references a value in its enclosing scope. 
The criteria that must be met to create closure in Python are summarized in the following points.
##		We must have a nested function (function inside a function).
##		The nested function must refer to a value defined in the enclosing function.
##		The enclosing function must return the nested function. 
'''
##Closure ex1
def func1(msg):
    '''this is my first func1'''
    print 'i am func1()'   
    
    def func2(name):
	    '''this is my second func2'''
	    print "I am func2"
	    print msg + " " + name

    return func2

nest_func = func1("Hello")
#del func1
print nest_func #Will print address of func2
nest_func("Rahul")

##Closure Ex2
def multiply_of(n):
    def multiply_with(x):
        print "\nn is: ", n
        print "x is: ", x
        return x*n
    return multiply_with


mult = multiply_of(3)
print mult(5)
print mult(15)
