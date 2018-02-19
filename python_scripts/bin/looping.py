#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

list1 = ['a','b','c']
list2 = ['orange','apple','grape']
for i, v in enumerate(list1):
    print i, v

#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
for q,a in zip(list1,list2):
    print 'What is your {0}?  It is {1}.'.format(q, a)

for q,a in zip(list1,list2):
    print 'What is your %s?  It is %s' % (q, a)

#To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for i in reversed(list1):
    print i

#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
for i in sorted(list2):
    print i

#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the iteritems() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v

