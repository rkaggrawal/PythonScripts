#!/usr/bin/python

def hi():
    print "Inside Hi"
    return "hi root"
def doSomethingBeforeHi (func):
    print "Before Hi !"
    return func()

fucn_out = doSomethingBeforeHi(hi) #This will retutn the function "hi" address
print fucn_out
#print fucn_out #Will print address of "hi" function
#retval = fucn_out() #It is similar of calling hi(), This Will execute hi function and will print whatever is inside hi() function.
#print retval

# 1
print "\ncase 1:"
def a_new_decorator(a_func):	
    def wrapTheFunction():
        print "I am doing some  boring work before executing a_func()"
        a_func()
        print "I am doing some boring work after executing a_func()"
    print "returning wrapTheFunction"	
    return wrapTheFunction

def a_function_requiring_decoration():
    print "I am the function which needs some decoration to remove my foul smell"

#a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
#a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction() 

#a_function_requiring_decoration
#outputs:I am doing some  boring work before executing a_function_requiring_decoration()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_function_requiring_decoration()



# 2
print "\ncase 2:"
def a_new_decorator(a_func):
    print "i am in a_new_decorator"
    def wrapTheFunction():
        print "I am doing some  boring work before executing a_func()"
        a_func()
        print "I am doing some boring work after executing a_func()"
    return wrapTheFunction
@a_new_decorator
def a_function_requiring_decoration():
    print "I am the function which needs some decoration to remove my foul smell"
a_function_requiring_decoration()

#a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"

#a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction() 

#a_function_requiring_decoration()
#outputs:I am doing some  boring work before executing a_function_requiring_decoration()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_function_requiring_decoration()



# 3 Nested decorators
print "\nNested decorators output: "
def bread(func):
    print "I am in bread func"
    def bread_wrapper():
        print "i am in bread_wrapper"
        func()
        print "i am out bread_wrapper"
    return bread_wrapper

def ingredients(func):
    print "I am in ingredients func"
    def ingredients_wrapper():
        print "i am in ingredients_wrapper"
        func()
        print "i am out ingredients_wrapper"
    return ingredients_wrapper

def sandwich(food="i am in sandwich"):
    print food

sandwich = bread(ingredients(sandwich))
sandwich()


#Output:
#i am in bread_wrapper
#i am in ingredients_wrapper
#i am in sandwich
#i am out ingredients_wrapper
#i am out bread_wrapper


# 3 Nested decorators using @

print "\nNested decorators using @ output: "
def bread(func):
    print "I am in bread func"
    def bread_wrapper(*arg, **kwargs):
        print "i am in bread_wrapper"
        for var in arg:
            print "i am",var," years old"
        for k,v in sorted(kwargs.iteritems()):
            print k + "=" + v
        func(*arg, **kwargs)
        print "i am out bread_wrapper"
    return bread_wrapper

def ingredients(func):
    print "I am in ingredients func"
    def ingredients_wrapper(*arg, **kwargs):
        print "i am in ingredients_wrapper"
        func(*arg, **kwargs)
        print "i am out ingredients_wrapper"
    return ingredients_wrapper

@bread
@ingredients
#def sandwich(food="I am in sandwich"):
def sandwich(*age, **kw):
    for var in age:
        print "i am",var," years old" 
    for k,v in sorted(kw.iteritems()):
        print k + "=" + v
l = [10,20]
d = {"fname":"rahul", "lname":'aggrawal'}    
sandwich(*l, **d)
