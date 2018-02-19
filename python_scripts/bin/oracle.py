#!/usr/bin/python

import os
import time
import cx_Oracle
con = cx_Oracle.connect('oastoltp/oastoltp@10.209.246.137/oastdb')
print con.version
cur = con.cursor()
cur.execute("select username from dba_users")

#for result in cur:
#	print result

row1 = cur.fetchone()
print "row1 is: ",row1
row2 = cur.fetchone()
print "row2 is: ",row2

res = cur.fetchmany(numRows=3)
print res

res = cur.fetchall()
print res

for r in res:
	print r
cur.execute("select * from global_name")
for result in cur:
	print "db name is: ",result

cur.close()
con.close()

#print "tims is ",time.time()
