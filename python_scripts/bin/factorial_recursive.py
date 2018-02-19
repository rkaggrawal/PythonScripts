#!/usr/bin/python

factorial_cache = {}

def fact(num):
    if num in factorial_cache:
        return factorial_cache[num]
    if num == 0:
        return 1
    else:
        value = num * fact(num-1)
    factorial_cache[num] = value

    return value

# print fact(998)

for i in range(1, 1001):
    print '{} : {}'.format(i, fact(i))


