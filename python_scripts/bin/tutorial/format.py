#!/usr/bin/python
import datetime
print('x: %d, y:%d' %(3,-1))

print '\nformat'
print('I am {} {} {}'.format('Rajat', 'Kumar', 'Gupta'))
print('I am {0} {1} {2}'.format('Rajat', 'Kumar', 'Gupta'))
print('I am {2} {0} {1}'.format('Rajat', 'Kumar', 'Gupta'))
print('I am {2} {0} {1} {1}'.format('Rajat', 'Kumar', 'Gupta'))


print '\nLocal variabe format'
fname='Rajat'
lname='Gupta'
print('I am {fname} {lname}'.format(**locals())) #All local variables

print '\nkeyword format'
print('I am {fname} {mname} {sname}'.format(fname='Rajat', sname = 'Gupta', mname='Kumar'))

print "\ndictionary format"
name = {'fname':'Rajat', 'mname':'kumar', 'sname':'Gupta'}
print('I am {} {} {}'.format(name, name, name))
print('I am {0} {1} {2}'.format(name, name, name))
print('I am {[fname]} {[mname]} {[sname]}'.format(name, name, name))
print('I am {0[fname]} {1[mname]} {2[sname]}'.format(name, name, name))
print('I am {0[fname]} {0[mname]} {0[sname]}'.format(name))
print('I am {fname} {mname} {sname}'.format(**name)) #Unpack dictionary
print('I am {fname} {mname} {sname}'.format(**{'fname':'Raj', 'sname':'Sharma', 'mname':'Ratan'})) #Unpacked dictionary


print "\nlist format"
list = ['Jenny', '30']
print 'I am {} and I am {} years old'.format(list,list)
print 'I am {0} and I am {1} years old'.format(list,list)
print 'I am {0[0]} and I am {1[1]} years old'.format(list,list)
print 'I am {0[0]} and I am {0[1]} years old'.format(list)
print 'I am {} and I am {} years old'.format(*list) #Unpack list
print 'I am {0} and I am {1} years old'.format(*list) #Unpack list


print '\nClass attribute format'
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Jack', 30)
print 'My name is {0.name} and I am {0.age} years old'.format(p1)

print '\nDigit format'
for i in range(7,11,1):
    print 'Value is {:02}'.format(i)
    print 'Value is {:02.4f}'.format(i)

print '\nDecimal Format'
pi = 3.14159265
print 'Pi is {}'.format(pi)
print 'Pi is {:.2f}'.format(pi)
print 'Pi is {:.3f}'.format(pi)

num = 1000000000
print 'Num is {:,}'.format(num)
print 'Num is {:,.2f}'.format(num)


print '\nDate format'
my_date = datetime.datetime(2016, 9, 30, 12, 30, 45)
print my_date

#September 30, 2016
print '{:%B %d, %Y}'.format(my_date)
print '\n{}'.format(datetime.datetime.now())
print '{:%Y-%m-%d}'.format(datetime.datetime.now())

#September 30, 2016 fell on Friday and was the 274 day of the year
print '{:%B %d, %Y fell on %A and was the %j day of the year}'.format(my_date)
print '{0:%B %d, %Y} fell on {0:%A} and was the {0:%j} day of the year'.format(my_date)




print'\nString format'
print '{:>20}'.format('Rajat Gupta') #print 20 character lengthy string
print '{:^20}'.format('Rajat') #print string in center


print '\nDecimal, Hexa, Octal, Binary format'
print 'int: {0:d}, hex: {0:x}, oct: {0:o}, bin: {0:b}'.format(42)


