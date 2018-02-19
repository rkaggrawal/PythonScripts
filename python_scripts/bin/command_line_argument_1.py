#!/usr/bin/python

import sys

print "Total argument are: ", str(sys.argv)

for arg in sys.argv:
    print arg

for count in range(len(sys.argv)):
    print sys.argv[count]
