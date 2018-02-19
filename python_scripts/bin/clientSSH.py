#!/usr/bin/python

import paramiko

def ssh_comm(ip, usr, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=usr, password=passwd)
    stdin, stdout, stderr = client.exec_command(cmd)
    return stdout

ssh_comm('10.0.2.15', 'rahul', 'vcs123', 'ifconfig')