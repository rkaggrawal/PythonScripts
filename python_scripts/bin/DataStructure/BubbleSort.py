#!/usr/bin/python

def bubble_sort(lst):
    for i in range (len(lst)):
        for j in range(len(lst)-i-1):
            # print a[j],a[j]
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print lst

    return lst


list = [38, 27, 43, 3, 9, 82, 10,0, 5]

print bubble_sort(list)