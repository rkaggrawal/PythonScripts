#!/usr/bin/python

class TTEmp(object):

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
    
emp1 = TTEmp()
emp1.fullname = 'Rajat Kumar'

print emp1.first
print emp1.last
#print emp1.email()
print emp1.email
#print emp1.fullname()
print emp1.fullname
