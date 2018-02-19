#!/usr/bin/python

def square(n):
    return n*n


if __name__ == '__main__':
    import doctest
    doctest.testmod()




#python -m doctest -v square.py
