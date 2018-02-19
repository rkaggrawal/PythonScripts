#!/usr/bin/python

'''
>>> False
False
>>> True
True
>>>
>>> False # doctest: +DONT_ACCEPT_TRUE_FOR_1
False
>>> True # doctest: +DONT_ACCEPT_TRUE_FOR_1
True

'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()