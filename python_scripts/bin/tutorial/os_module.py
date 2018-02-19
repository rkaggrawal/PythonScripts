#!/usr/bin/pytho
import os
from datetime import datetime

print os.stat('/var/log/auth.log')
print os.stat('/var/log/auth.log').st_mtime
print datetime.fromtimestamp(os.stat('/var/log/auth.log').st_mtime)


print os.getcwd()
os.chdir('/home/rahul/Documents')
print os.getcwd()


print os.environ.get('HOME')
file_path = os.path.join(os.environ.get('HOME'), 'testfile.txt')
print file_path
#os.mknod(file_path)


print os.path.basename('/tmp/text.txt')
print os.path.dirname('/tmp/text.txt')
print os.path.split('/tmp/text.txt')
print os.path.splitext('/tmp/text.txt')
print os.path.exists('/tmp/text.txt')
print os.path.exists(file_path)
print os.path.isdir(file_path)
print os.path.isfile(file_path)
print dir(os.path)


# for dirpath, dirnames, filename in os.walk('/home/rahul/Documents'):
#     print
#     print 'Currentpath: ', dirpath
#     print 'Directories: ', dirnames
#     print 'Files: ', filename
