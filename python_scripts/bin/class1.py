#!/usr/bin/python
import inspect
class A:
    def myfunc1(self, data):
        print "class A method"
        self.data = data
        return self.data

    def myfunc2(self, data):
        print "class B method"	
        self.data = data
        return self.data

a = A()
print a.myfunc1(10)
print a.data
A.name = "rahul"
print a.name
print a.__dict__
print A.__dict__ #name will be avaialble under class metdata but not in object "a" metdata

print "\n"
a.age = 20
print a.age
print a.__dict__
print A.__dict__# age will be avaialble under object metdata but not in class metdata

print "\n"
print a.myfunc2(20)
print a.data
