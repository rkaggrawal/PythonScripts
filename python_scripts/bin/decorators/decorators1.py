#!/usr/bin/python

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print "I am Wrapper"
        original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print 'display function ran'

display()
# display = decorator_function(display)
#
# display()

@decorator_function
def display_info(name, age):
    print 'my name is {} and age is {}'.format(name, age)

display_info('paul', 30)
