#!/usr/bin/python

import os

filename = "/etc/fstab"

if os.path.exists(filename):
	print "Check last mofified time of file: "+filename
	print os.path.getmtime(filename)
	#statbuf = os.stat(filename)
	#print "Modification time:",statbuf.st_mtime

else:
	raise Exception ("File does not exist !")
