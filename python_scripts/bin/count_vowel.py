#!/usr/bin/python

# string of vowels
vowels = 'aeiou'

#String to check vowels
ip_str = "This is a my vowel outline"

#make it suitable for caseless
ip_str = ip_str.lower()

# make a dictionary with each vowel a key and value 0
#count = {}
#count = count.fromkeys(vowels,0)
count = {}.fromkeys(vowels,0)

for char in ip_str:
    if char in count:
        count[char] += 1	

#print count for each vowel
print count
