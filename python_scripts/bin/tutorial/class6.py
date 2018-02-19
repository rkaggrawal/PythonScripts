#!/usr/bin/python

class Employee(object):

    def __init__(self,first=None,last=None):
        self.first = first
        self.last  = last
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    @fullname.setter
    def fullname(self, name):
        print "Setting Value"
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print "Deleting Value"
        self.first, self.last = None, None

    
emp_1 = Employee('Cory', 'Duggins')
print emp_1.email
print emp_1.fullname
emp_1.fullname = 'Jesica Duggins'
print emp_1.fullname
del emp_1.fullname
print emp_1.fullname

# emp_1.fullname = 'Rajat Kumar'
#
# print emp1.first
# print emp1.last
# #print emp1.email()
# print emp1.email
# #print emp1.fullname()
# print emp1.fullname
