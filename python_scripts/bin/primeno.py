#!/usr/bin/python

# num = int (raw_input("Enter a number\n"))
# #print "Number is: ",num
#
# if (num > 1):
# 	for i in range(2,num):
# 		if (num % i == 0):
# 			print num,"is divided by",i,"hence ",num,"is not a prime number !"
# 			quit("Exit program !")
# 	else:
# 		print num,"is a prime number"
#
# else:
# 	print "Enter value more than 1 !"


import time
#Method1
# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


#Method 2
# def is_prime(n):
#     if n == 1:
#         return False
#     max = int (n / 2)
#     for i in range(2, max+1):
#         if n % i == 0:
#             return False
#     return True

#Method3 - This method is most optimized.
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max = int(n / 2)
    for i in range(3, max+1, 2):
        if n % i == 0:
            return False
    return True

t0 = time.time()
for i in range(1, 11):
    # is_prime(i)
    print '{} : {}'.format(i, is_prime(i))
t1 = time.time()
print 'Time for execution: {}'.format(t1-t0)
