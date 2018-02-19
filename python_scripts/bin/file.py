#!/usr/bin/python

import os

print dir(os)
print help(os.chown	)
##Open and write in file
fo = open ("foo.txt","w+")
print "File name is: ",fo.name
print "File mode is: ",fo.mode
fo.write ("This is my first line\n")
fo.write ("This is my second line\n")
position = fo.tell()
print "Current file position : ", position
position = fo.seek(0)
str = fo.read()
print "Read file: \n",str
fo.close()

##Open and read from file
fo = open ("foo.txt","r+")
print "File mode is: ",fo.mode
position = fo.tell()
print "Current file position : ", position
str = fo.read()
print "Read file: \n",str
fo.close()

##Open and read from file
print "Start for - open"
for line in open ("foo.txt"):
	#print line
	print line.rstrip('\n').startswith('This')

with open ("foo.txt") as fp:
	for line in fp:
		print line.rstrip('\n')
##Remove file
#os.remove("foo.txt")
os.rename("foo.txt","newfoo.txt")
os.rmdir("test")
os.mkdir("test")

##List all files in a dir
os.chdir("/home/rahul/python_scripts/bin/openstack")
curdir = os.getcwd()
print "My current dir is: ",curdir
list_files = os.listdir(curdir)  ##returns list of file names
for file in (list_files):
	print file

dt = os.system('date')
print "Date is: ",dt
f = os.popen('date')
now = f.read()
print "Date is: ",now
os.system('ls /etc/resolv.conf')
#os.environ()
from subprocess import call
# print "Current time is:",call('date')
print call('date')

print open.__doc__