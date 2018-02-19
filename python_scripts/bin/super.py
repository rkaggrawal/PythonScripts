#/usr/bin/python

class Base(object):
    def __init__(self):
        print "Base created"
    def basemethod(self):
        print "Method from Base class"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(ab):
        super(ChildB, ab).__init__()
        super(ChildB, ab).basemethod()

Base().basemethod()

print "\n"
ChildA() 

print "\n"
ChildB()
