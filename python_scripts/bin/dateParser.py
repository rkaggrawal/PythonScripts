#!/usr/bin/python

from datetime import datetime
import time
now =  datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
min = str(now.minute)
sec = str(now.second)

#print datetime.__doc__
#print datetime.__dict__
print now.strftime("%Y/%m/%d %H:%M:%S")
print dd+"/"+mm+"/"+yyyy+" "+hour+":"+min+":"+sec

stime = time.time()
print "Start time: ",stime 

time.sleep(1)

#etime = time.time()
#print "End time: ",etime
#elptime = etime-stime
print "Elapsed time: {:1.4f}s ".format(time.time()-stime)

import calendar
print(calendar.month(2017,3))
print(calendar.calendar(2017,c=10, w=3, l=1))
print(calendar.isleap(2017))

