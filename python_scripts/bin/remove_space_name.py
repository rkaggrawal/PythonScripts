#!/usr/bin/python

import os,glob
import sys

try:
    dir_loc = sys.argv[1]
except IndexError:
    print "Please provide dir location"
    print "Usage: python remove_space_name.py <dir location>"
else:
    # os.chdir("/home/rahul/python_scripts")
    os.chdir(dir_loc)
    print os.getcwd()
    for file in glob.glob("*.csv"):
        print file
        l = file.split(' ')
        new_file = '_'.join(l)
        print new_file
        os.rename(file,new_file)