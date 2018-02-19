#!/usr/bin/python


####Local variable
##Here total we be treated as local variable in func so vlaue inside and outside function will be different.
print "####Local variable"
total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total
   #return total;

# Now you can call sum function
sum( 10, 20 );
print "Outside the function global total : ", total 



##Global variable
##Here total we be treated as global in func so vlaue inside and outside function we be same.
print "\n####Global variable"
total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   global total
   total = arg1 + arg2; # Here total is global variable.
   print "Inside the function local total : ", total
   #return total;

# Now you can call sum function
sum( 10, 20 );
print "Outside the function global total : ", total
