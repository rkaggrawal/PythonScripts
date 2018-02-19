#/usr/bin/python

import paramiko
from multiprocessing import Process
#import sys
#import time

#HOST = "10.209.172.201"
#USER = "root"
#PASS = "vcs123"

HOST = "dl560g9-06-vm10.vxindia.veritas.com"
USER = "root"
PASS = "Vrp@1234"

client1=paramiko.SSHClient()
#Add missing client key
client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#connect to switch
client1.connect(HOST,username=USER,password=PASS)
print "SSH connection to %s established" %HOST

stdin, stdout, stderr = client1.exec_command('ls /var/opt/VRTS/utrp\n')
#stdin, stdout, stderr = client1.exec_command('rpm -qa | grep -i VRTSitrptap\n')
#print stdout
rpm_out = stdout.read()
print rpm_out
#rpm_name = rpm_out.rstrip()
#print rpm_name
#cmd = "/bin/rpm -e "+rpm_name
#print cmd
#stdin, stdout, stderr = client1.exec_command(cmd)
#print stdout.read()
#print stderr.read()
