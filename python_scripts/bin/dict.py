#!/usr/bin/python

dict = {'fname':'rahul','lname':'aggrawal'}
print "Org dict is %s" % str(dict)
print "dict.items() ", dict.items() #Returns list of tuples. Key & Value are combined in one tuple.

tinydict = {'city':'pune','lname':'parida'}
dict3 = dict.items()+tinydict.items()
print "\ndict+tinydict: ",dict3

print "\n"
dict4 = dict.copy()
dict4.update(tinydict)
print "dict4:  ",dict4

print "\n"
print "Add mname"
dict['mname'] = "kumar"
print "After modification dict is"," ",dict
print "First name is"," : ",dict['fname']
print "Keys of dict are"," ",dict.keys()
print "Values of dict are"," ",dict.values()
print "len of dict is  ",len(dict)

print "\n\n"
###dict.get()
print "Dict is"," ",dict
print "dict.get('lname'): ",dict.get('lname')
print "dict.get('gname','not found'): ",dict.get('gname', 'not found')#gname does not exits in dict hence will return default value 'not found'

print "\n\n"
##dict.setdefault(key, default=None)
#This method returns the key value available in the dictionary and if given key is not available then it will return provided default value.
print "dict.setdefault('lname'): ",dict.setdefault('lname')
print "dict.setdefault('city','pune'): ",dict.setdefault('city', 'pune') #As 'city' does not exist in dict, it will add city:pune in dict.
print "Dict is"," ",dict

print "\n\n"
##dict.keys()
print "Keys of dict are"," ",dict.keys()
##dict.values()
print "Values of dict are"," ",dict.values()

print "\n\n"
##dict.has_key()
#This method return true if a given key is available in the dictionary, otherwise it returns a false.
print "dict.has_key('lname'): ",dict.has_key('lname')
print "dict.has_key('pname'): ",dict.has_key('pname')

print "\n\n"
##dict.fromkeys(seq[, value]))
#The method fromkeys() creates a new dictionary with keys from seq and values set to value.
vowel = {}.fromkeys('aeiou')
print "vowel dict is: %s" % str(vowel)
vowel = {}.fromkeys('aeiou',1)
print "vowel dict is: %s" % str(vowel)
vowel = {}.fromkeys([10,20,30],1)
print "vowel dict is: %s" % str(vowel)
vowel = {}.fromkeys(('x','y','z'),1)
print "vowel dict is: %s" % str(vowel)

print "\n\n"
##dict.items()
#The method items() returns a list of dict's (key, value) tuple pairs
print "dict.items() : ",dict.items()
print "dict.iteritems() : ", dict.iteritems()
print "dict.iteritems() : ",[x for x in dict.iteritems()]

print "\n\n"
##dict.update()
#The method update() adds dictionary dict1's key-values pairs in to dict. This function does not return anything.
#This method does not return any value.
dict1 = {'locality':'baner'}
dict.update(dict1)
print "after update dict is: ", dict

##change dict value
dict['locality'] = 'balewadi'
print "after changing value dict is: ", dict


##dict.copy()
#The method copy() returns a shallow copy of the dictionary.
dict2 = dict1.copy()
print "New dictionary is: ",dict2

print "\n\n"
##dict.clear()
#The method clear() removes all items from the dictionary.
print "Before clear dict is: ",dict2
dict2.clear()
print "After clear dict is: ",dict2

#delete item from dictionary
del dict1['locality']
print "dict1 is: ", dict1

##delete complete dictionary
del dict2
#print "After delete dict is: ",dict2 #Will print error as dict2 is deleted


print "\n\n"
print dir(dict)

d = {"name":"rahul"}
print (d.setdefault("lname", "aggrawal"))
print(d)

