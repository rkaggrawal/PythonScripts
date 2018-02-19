#!/usr/bin/python

the_generator = (x+x for x in range(3)) #() is for generator and, [] for list comprehension

print type(the_generator)

for element in the_generator:
    print element

#len(the_generator) #It will fail beacuse the generator is iterable, it is not a collection, and thus has no length.

print "\n"
def search(keyword, filename): #search is generator function. When we use yield in any function that turns into generator function
    print "generator started"
    #f = open(filename, 'r')
    count = 1
    for line in open(filename):
        if keyword in line:
            print "Before yield"
            yield count,line.strip("\n\r")	#it gets paused after this until you call the_gen.next()
            print "\nAfter yield"
        count+=1
    #f.close()

the_gen = search('cricket', 'gentest.txt') #the_gen is a generator object
print type (search)
print type(the_gen)

print "\n"
print the_gen.next()
print the_gen.next()
print the_gen.next()
# #print the_gen.next()

'''
##fibonacci example using iterators
def fibonacci(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield prev
        prev, curr = curr, prev + curr
        counter += 1

fib_gen = fibonacci(100)
print fib_gen.next()
print fib_gen.next()
print fib_gen.next()
print fib_gen.next()
'''
