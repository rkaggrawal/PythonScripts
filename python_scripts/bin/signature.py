#!/usr/bin/python
import inspect


def foo(a, b, c='blah1', x='blah2', *arg):
    pass


print(inspect.getargspec(foo))
