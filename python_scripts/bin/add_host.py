#!/usr/bin/python

import os

##Open and write in file
#fo = open ("add_host.csv","w+")
#print "File name is: ",fo.name
#print "File mode is: ",fo.mode
#fo.write ("Hostname,Username,Password\n")
#fo.close()

fo = open ("add_host_svm11_svm70.txt","w+")
vmlist = range(11,71)

for vmname in (vmlist):
	vmcred = "svm"+str(vmname)+".vrp.veritas.com,root,vrp@123"
	fo.write(vmcred)
	fo.write("\n")
fo.close()
