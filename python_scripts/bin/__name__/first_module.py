#!/usr/bin/python
__author__ = "Rahul"

def func():
    print "First module name: {}".format(__name__)

if __name__ == '__main__':
    func()
    print "Run directly"
else:
    print "Run from Import"