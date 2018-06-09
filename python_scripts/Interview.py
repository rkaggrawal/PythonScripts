#from __future__ import print_function
# #
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# # A1 = range(10)
# # A2 = sorted([i for i in A1 if i in A0])
# # A3 = sorted([A0[s] for s in A0])
# # A4 = [i for i in A1 if i in A3]
# # A5 = {i:i*i for i in A1}
# # A6 = [[i,i*i] for i in A1]
# # A0 = dict(zip(('a','b','c','d','e','f'),(1,2,3,4,5)))
# # print 'A0= {}'.format(A0)
# # print 'A1= {}'.format(A1)
# # print 'A2= {}'.format(A2)
# # print 'A3= {}'.format(A3)
# # print 'A4= {}'.format(A4)
# # print 'A5= {}'.format(A5)
#
# ###########
# # def f(x,l=[]):
# #     for i in range(x):
# #         l.append(i*i)
# #     print(l)
# #
# # f(2)
# # f(3,[3,2,1])
# # f(3)
#
# ################
# # list = ['a', 'b', 'c', 'd']
# # print list[10:]
# #
# # len(1011)
#
# print reduce(lambda x, y: x * y, range(1, 6))
#
# str1 = "python"
# str_len = len(str1)
#
# for x in range(str_len):
#     print str1[:x + 1]
#
# num = 12345
# print type(num)
# print map(int, nstr(num))
# list1 = list(nstr(num))
# print list1.__class__
# print list1
#
# nstr = "abcdefghijklmnopqrstuvwxvzabcde"
# print len(nstr)
#
# d1 = {1: 1}
# l1 = [2, 3]
# d1.update({x: x ** 2 for x in l1})
# print d1
#
# x = 123456
#
# # print list(str(x))
# # print x.split()
#
# mystr = "python"
# mylist = list(mystr)
# # print mylist
# for i, v in enumerate(mylist):
#     if v == "p":
#         # print i, v
#         mylist[i] = 'j'
#         break
#
# # print mylist
# print ''.join(mylist) + "\n\n"

row = 5
ele = 1
for row_num in range(row):
    # ele = 1
    for col_num in range(row_num):
        print ele,
        ele += 1
    print ""
