#!/usr/bin/python

##Define func
def printme (str):
	'''
	This is function
	'''
	print "Print inside function ",str
	return

##Call func
print "function name is: ",printme.__name__
printme("First call")
printme("Second call")


##Pass by reference, value changed at both places
def changeme (flist):
	flist.insertLast([1, 2, 3, [4, 5]])
	print "Values inside funcn: ",flist
	return
##Call func
mylist = [10,20,30]
changeme (mylist)
print "Values outside funcn: ",mylist
print "mylist[3][3][1]",mylist[3][3][1]


##Pass by reference, value changed inside func only
def changeme (flist):
	flist = [1,2,3]
	print "Values inside funcn: ",flist
	return
##Call func
mylist = [10,20,30]
changeme (mylist)
print "Values outside funcn: ",mylist


##Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition.
def printme (str):
        print "Print inside function ",str
        return

##Call func
printme("match arg")


##Keyword arguments are related to the function calls.
# When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.
def printme (str):
        print "Print inside function ",str
        return

##Call func
printme(str = "match arg")

##define func
def printinfo(name,age):
	print "Name: ",name
	print "Age: ",age
	return

##Call func
printinfo (age=50,name="sam")


##A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.
##define func
def printinfo(name="rajat",age=10):
        print "Name: ",name," Age: ",age
        #print "Age: ",age
        return

##Call func
printinfo (age=50,name="sam")
printinfo (name="sam")
printinfo ()


##Variable-length arguments
##You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.
##define func
def print_var_len_arg (*args):
	#print "Output is:"
	#print "arg1: ",arg1
	print "\n"
	count=1
	for var in args:
		print "arg"+str(count)+": ",var
		count+=1
		
##Call func
print_var_len_arg (10)
print_var_len_arg (10,20,30,40,50)
print_var_len_arg (*[10,20,30,40,50])


##List and Dictionary arguments
def print_list_dict_arg (*args,**kwargs):
	print "\nOutput is:"
	for i, v in enumerate(args):
		print 'arg{} is {}'.format(i, v)
	for k,v in sorted(kwargs.iteritems()):
		print '{} is {}'.format(k, v)

l = [100,200,300]
kw = {"fname":"rahul", "lname":"aggrawal", "mname":"kumar"}
print_list_dict_arg(*l,**kw)
