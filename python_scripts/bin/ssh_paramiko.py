#/usr/bin/python

import paramiko

#HOST = "10.209.172.201"
#USER = "root"
#PASS = "vcs123"

HOST = "10.209.245.66"
USER = "root"
PASS = "vrp@123"

ssh=paramiko.SSHClient()

#Add missing client key
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#connect hist
#ssh.connect(HOST, port=22, username=USER, password=PASS)
ssh.connect(HOST, username=USER, password=PASS)
print "SSH connection to %s established" %HOST

stdin, stdout, stderr = ssh.exec_command('ifconfig')
output=stdout.readlines()
print type(output)
print '\n'.join(output)

stdin, stdout, stderr = ssh.exec_command('who -u')
output=stdout.readlines()
print type(output)
print '\n'.join(output)


stdin, stdout, stderr = ssh.exec_command('rm /root/testfile')
stdin.write('yes')
stdin.write('\n')
stdin.flush()
output = stdout.readlines()
print '\n'.join(output)
#print "Removed file /root/testfile successfully"

ssh.close()

#stdin, stdout, stderr = client1.exec_command('rpm -qa | grep -i VRTSitrptap\n')
#print stdout
#rpm_out = stdout.read()
#print rpm_out
#rpm_name = rpm_out.rstrip()
#print rpm_name
#cmd = "/bin/rpm -e "+rpm_name
#print cmd
#stdin, stdout, stderr = client1.exec_command(cmd)
#print stdout.read()
#print stderr.read()
