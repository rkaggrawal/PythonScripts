#!/usr/bin/python

def insertion_sort(lst):
    print('{}-org'.format(lst))
    for i in range(1, len(lst)):
        key = lst[i]
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
        print lst
    return lst


list = [38, 27, 43, 3, 9, 82, 10, 0, 5]

print insertion_sort(list)