#!/usr/bin/python
def func1(str, list1, list2):
    #Method1
    print '\nCalling Method1'
    for x,y in zip(list1, list2):
        print x,y
        if  x != y:
            print "\"{}\" is not palidrome".format(str)
            break
    else:
        print "\"{}\" is palidrome".format(str)

    #Method2
    print '\nCalling Method2'
    if list1 == list2:
        print "\"{}\" is palidrome".format(str)
    else:
        print "\"{}\" is not palidrome".format(str)


if __name__ == "__main__":
    input = ["civic", "civiczz", 16461]

    for x in input:
        list1 = list(str(x))
        list2 = list1[::-1] #reverse list
        print "\n",list1
        print list2
        func1(x, list1, list2)
