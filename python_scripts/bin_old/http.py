#!/usr/bin/python

import urllib2

IP='10.209.83.205'
response = urllib2.urlopen("http://%s/testResults/SLES12VM3_LxRT-6.2.1-2015-04-23a_27-04-2015-20:59/RESULTS/" %(IP))
data = response.read()
#print data

fname="httpdata.txt"
FH=open(fname,"w")
FH.write(data)
FH.close()
