#!/usr/bin/pythoon

print r'A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.'+"\n\n"


print 'org list is: basket = [\'apple\', \'orange\', \'apple\', \'pear\', \'orange\', \'banana\']'
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print fruit
print r"orange in fruit:",'orange' in fruit
print r"grape in fruit:" ,'grape' in fruit

print "\n"
print dir(set)

print "\n"
# list1 = [2, 4, 6, 8]
set1 = {2, 4, 6, 8}

# list2 = [1,2,3,4]
set2 = {1, 2, 3, 4}

print set1.intersection(set2)
print set1.difference(set2)
print set2.difference(set1)
print set1.union(set2)