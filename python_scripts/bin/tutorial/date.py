#!/usr/bin/python
import datetime
import pytz

print '#'*5 + 'Date' + '#'*5
d = datetime.date(2016, 7, 30)
print d
print d.year
print d.month
print d.day

print "\n"
tday = datetime.date.today()
print tday
print tday.weekday()
print tday.isoweekday()

print "\n"
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)
bday = datetime.date(2016, 10, 17)
till_day = bday - d
print till_day
print till_day.days
print till_day.total_seconds()


print '\n'+'#'*5 + 'Time' + '#'*5
t = datetime.time(17, 15, 40, 320000)
print t
print t.hour
print t.minute
print t.second
print t.microsecond


print '\n'+'#'*5 + 'Date and Time' + '#'*5
dt = datetime.datetime(2016, 7, 25, 16, 45, 19, 170000)
print dt
print dt.strftime("%Y/%m/%d %H:%M:%S:%f")
print dt.date()
print dt.year
print dt.month
print dt.day

print "\n"
print dt.time()
print dt.hour
print dt.minute
print dt.second

print "\n"
tdelta = datetime.timedelta(days=10)
print dt + tdelta
tdelta = datetime.timedelta(hours=12)
print dt + tdelta
tdelta = datetime.timedelta(days=10, hours=12)
print dt + tdelta


print '\nCurrent date and time'
dt_today = datetime.datetime.today()
print dt_today

dt_now = datetime.datetime.now(tz=pytz.UTC)
print dt_now

dt_india = dt_now.astimezone(pytz.timezone('Asia/Kolkata'))
print dt_india

# for tz in pytz.all_timezones:
#     print tz

print "\n"+"###"*5 + "Time module" + "###"*5
import time
print time.time()
print time.asctime()
print time.localtime(time.time())


