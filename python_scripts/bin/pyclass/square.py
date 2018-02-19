#!/usr/bin/python



def square(n):
    '''
    >>> square(1)
    1
    >>> square(2)
    4
    >>> square(3)
    9
    >>> square(4)
    16
    >>> square()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: square() takes exactly 1 argument (0 given)
    >>> square('x')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "square.py", line 4, in square
        return n*n
    TypeError: can't multiply sequence by non-int of type 'str'

    :param n:
    :return:
    '''
    # return n*n
    return n**2

if __name__ == '__main__':
    import doctest
    doctest.testmod()



# python square.py -v
#python -m doctest -v square.py
