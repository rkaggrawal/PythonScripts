#/usr/bin/python

import SSHLibrary

s = ssh.Conncetion('localhost','root',password='vcs123')
print "Files are: ",s.execute('ls -l /home/raggrawa/python_scripts/bin')
s.close()
