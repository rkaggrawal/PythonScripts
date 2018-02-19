#!/usr/bin/python

class foo:
    def __init__(self, a, b, c):
        print 'I am in __init__'
        self.a = a
    def __call__(self, *args, **kwargs):
        print 'I am in foo:__call__'
    # if True:
    #     print 'Value of a is: {}'.format(a)

x=foo(1,2,3)
x()



class foo1:
    def __call__(self, a, b, c):
        print 'I am in foo1:__call__'

y = foo1()
y(1,2,3)