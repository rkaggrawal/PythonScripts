#/usr/bin/python

class A:
   message = "class message"
   nInstances = 0
   def __init__(self, name = 'Rahul'):
      A.nInstances = A.nInstances + 1
      self.name = name
   @classmethod
   def cfoo(cls):  #You can replace 'cls' by any name like clss or my_class as this is just a reference of class.
      print "test classmethod", cls
      print cls.message, cls.nInstances
   
   def foo(self, msg):
      self.message = msg
      print(self.message)
      # print(msg)

   def __str__(self):
      return self.message
   
   @staticmethod
   def howManyInstances():
      print 'Number of instances created: ', A.nInstances

print A.message
#Traditional call
a = A()
b = A()
c = A()

#print a
b.foo("Calling foo method")

#Unbound method call
A.foo(b, "calling foo")

print "\n"
#Using @classmethod. Class method here cfoo, can be called directly without creating the class object.
a.cfoo()
A.cfoo()

print "\n"
#Using @staticmethod
b.howManyInstances()
A.howManyInstances()
