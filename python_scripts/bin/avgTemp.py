#!/usr/bin/python
import os
city = "pune"

city_temp = 0
city_count = 0
country = str
for line in open("temp.txt", "r"):
    if city in line:
        line.strip('\n')
        list = []
	list = line.split(" ")
	list = [word.strip() for word in list]
	city_count += 1
	city_temp += float(list[1])
else:
    avgtemp = float (city_temp/city_count)
    print "Avg temp of %s is %s" %(city,str(avgtemp))
    country = list[2]
 

country_temp = 0
country_count = 0
for line in open("temp.txt", "r"):
    if country in line:
        line.strip('\n')
        list = []
	list = line.split(" ")
	list = [word.strip() for word in list]
	country_count += 1
	country_temp += float(list[1])
else:
    avgtemp = float (country_temp/country_count)
    print "Avg temp of %s is %0.2f"  %(country,avgtemp)
