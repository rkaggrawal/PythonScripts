#!/usr/bin/python

def selection_sort(lst):
    for i in range(len(lst)):
        min_indx = i
        for j in range(i+1, len(lst)):
            if lst[min_indx] > lst[j]:
                min_indx = j
        lst[i], lst[min_indx] = lst[min_indx], lst[i]
        print lst
    return lst


list = [38, 27, 43, 3, 9, 82, 10, -1]

print selection_sort(list)