#!/usr/bin/python
import time
# sum=0
# for num in range(1,1000):
#     if num%3 ==0 or num%5 ==0:
#         sum+=num
#
# print "total is: {}".format(sum)

# def triangle_number(num):
#     sum=0
#     for i in range(1, num+1):
#         sum+=i
#     return int(sum)

multiply_cache = {}
def triangle_number(num):

    if num in multiply_cache:
        return multiply_cache[num]

    if num == 1:
        return 1

    if num > 1:
        sum = num + triangle_number(num-1)

    multiply_cache[num] = sum
    return sum


t0 = time.time()
for n in range(1,10001):
    total = triangle_number(n)
    print "Traingle of {} is {}".format(n, total)
    list=[]
    for t in range(1, total+1):
        if total%t == 0:
            list.append(t)
    if len(list) >= 200:
        print "{} are total factor of {} => {}".format(len(list),total,list)
        t1 = time.time()
        print 'Time for execution: {}'.format(t1 - t0)
        break




