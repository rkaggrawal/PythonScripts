#!/usr/bin/python

nums = [1,5,3,2,4]
# print dir(nums)

# print max(nums)
# print min(nums)
# print sum(nums)


# print dir(dict)
# help(dict)
# print dir(set)
# help(set)

# print dir(str)
# help(str.rsplit)
help(str.title)
# help('print')
with open('/home/rahul/python_scripts/testfile', 'r') as rf:
    print 'File: {} \nMode: {}'.format(rf.name, rf.mode)
    chunk_size = 20
    rf_chunk = rf.read(chunk_size)
    while len(rf_chunk) > 0:
        print rf_chunk.rstrip('\n')
        # print rf.tell()
        rf_chunk = rf.read(chunk_size)
    # print rf.readline().rstrip('\n') #Read one line and Removes new line chracter
    # print rf.readline().rstrip('\n')
    # print rf.read() #Read all lines

print rf.closed #Returns true if file is closed, false otherwise.
# print rf.read()

str1 = "my name is Sachin" #Convert first letter of each word to UpperCase
print str1.title() #Method1
#print ' '.join([s[0].upper() + s[1:]for s in str1.split(' ')]) #Method2

f_num = ['#1', '#2', '#10']
print f_num[0].strip()[1:].zfill(2)
import sys, os, random, math, calendar
print os.__file__
from datetime import datetime
# print dir(random)
# help(random.randint)
# print random.randint(1, 50)
# help(random.choice)
print random.choice(range(100, 200))
# print dir(sys)
# print dir(os)
help(os.path.splitext)
print os.path.join('/home', 'raggrawal')
print datetime.fromtimestamp(os.path.getmtime('dir_help.py'))
# print sys.path
# sys.path.append