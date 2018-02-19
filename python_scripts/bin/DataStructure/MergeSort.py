#!/usr/bin/python

def merge(left, right):
    result = []
    i, j = 0, 0
    print "\n", left, ":", right
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    print 'result= {}'.format(result)
    return result


def mergesort(lst):
    if len(lst) == 1:
        return lst
    mid = int(len(lst)/2)
    # print lst[:mid], ":", lst[mid:]
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    # print left, ":" ,right
    return merge(left, right)


list = [38, 27, 43, 3, 9, 82, 10]
print "Sorted list is: {}".format(mergesort(list))