#!/usr/bin/python

from random import randint

items = []
for value in range(0, 10):
    item = randint(0, 1000) #any avlue between 0 to 1000
    items.append(item)
else:
    print items

