#!/usr/bin/python
import inspect
class A(object):
    age=5
    def myfunc(self):
        print "class A method"
class B:
    def myfunc(self):
        print "class B method"
class D:
    def myfunc(self):
        print "class B method"
class C(B,A):
    pass

print "My class name via A.__name__:",A.__name__
print help(C)
x = C()
x.myfunc()
print C.age
print x.age

print "\nInstance test"
print isinstance(x, C)
print isinstance(x, A)
print isinstance(x, B)
print isinstance(x, object)
print isinstance(x, D)

print "\nInstance Test for types"
print isinstance(1,type(55))
print isinstance(1,(int,float,long))
print isinstance('x',type(55))
print isinstance('x',type('55'))



print "\nSubclass test"
print issubclass(C, A)
print issubclass(C, B)
print issubclass(A, object)
print issubclass(C, D)


print r'hasattr(x, age): ',hasattr(x, 'age')
print "\n"
if hasattr(x, 'age') is True:
    print r'getattr(x, \'age\'): ',getattr(x, 'age')
    print r'setattr(x, \'age\',50): ',setattr(x, 'age',50)
    print r'getattr(x, \'age\'): ',getattr(x, 'age')
    print r'delattr(x, \'age\'): ',delattr(x, 'age') #This will delete value of 'age' variable and set it to previous value. In this case will reset to value 5.
    print r'hasattr(x, \'age\'): ',hasattr(x, 'age')
    print r'getattr(x, \'age\'): ',getattr(x, 'age')


if 'rahul' in ['rahul','aggrawal']:
    print "Name Found"

print "####Local variable"
#print(inspect.getargspec(x))
