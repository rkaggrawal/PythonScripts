#!/usr/bin/python

dict = {'abcd':'1234','ABCD':'SYMC'}
tinydict = {'Perl':'Pyhton'}
print dict
print dict.keys();
print dict.values();
dict['abcd'] = 'english'
print "After modification dict is:\n",dict
dict ['Name'] = "Rahul"
print "After modification dict is:\n",dict
del dict['Name']
print "After modification dict is:\n",dict
dict.clear();
print "After modification dict is:\n",dict


