#!/usr/bin/python

print r'Method Overloading is when same method name is used for 2 or more times in the same class with different number of arguments.'

print r'Method override occurs when the derived class writes its own version of a method which has already been defined in the parent class. Both the methods in base class and derived class must have same declaration.'

class a:
    def cl(self,var):
        print "first cl",var
    def c1(self,var1,var2):
	print "first cl overload",var

class b(a):
    pass
    def cl(self,var):
	print "second cl",var

##Python does not support method overloading
##Following call will fail as it will always go with first c1 method not for second c1
## Uncomment below two lines to test method overloading
# obj = a()
# obj.cl(5,6)


##Pytho supports method overriding
##Following Call will run for method overriding
obj = b()
obj.cl(5)

