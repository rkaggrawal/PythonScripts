#!/usr/bin/python

__all__ = ['Pot1'] 
'''
	When we do 'from Potss import *', it will import only Pot1 not Pot2.To import Pot2 we should write 'from Potss import Pot2' in __init__.py file.	
'''


def Pot1():
   print "I'm Pot1 Phone"

def Pot2():
   print "I'm Pot2 Phone"

