#!/usr/bin/env python 
# -*- coding: utf-8 -*

'''
Created on 2017年9月14日

@author: Saya
'''
# for i in range(1,5):    
#     for j in range(1,5):
#         for k in range(1,5):
#             #if( i != k ) and (i != j) and (j != k):
#              if i!=j!=k:
#                 print (i,j,k)

# d=[]
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if (a!=b) and (a!=c) and (c!=b):
#                 d.append((a,b,c))
# print ("总数量：", len(d), d)

# list_num = (1,2,3,4)
# d = [    
#         i*100 + j*10 + k     
#         for i in list_num
#             for j in list_num 
#                 for k in list_num 
#                     if (i != j and j != k and k!= i)
#                                               
#     ] 
# print ("总数量：", len(d), d)

# num=(1,2,3,4)
# i=0
# for a in num:
#     for b in num:
#         for c in num:
#             if (a!=b) and (b!=c) and (c!=a):
#                 i+=1
#                 print(a,b,c)
# print("总数量：",i) 

# line=[]
# for i in range(123,433):
#     a=i%10
#     b=(i%100)//10
#     c=(i%1000)//100
#     if a!=b and b!=c and a!=c  and 0<a<5 and 0<b<5 :
#         line.append(i)
# print("总数量：",len(line), line)

#from itertools import permutations 
# for i in permutations([1, 2, 3, 4], 3):
#     print(i)
# line=[]
# for i in permutations([1, 2, 3, 4], 3):
#     k = ''
#     for j in range(0, len(i)):
#         k = k + str(i[j])
#     line.append(int(k))
# print("总数量：",len(line), line)

# #用集合去除重复元素
# import pprint
# list_num=['1','2','3','4']
# list_result=[]
# for i in list_num:
#     for j in list_num:
#         for k in list_num:
#             print(set(i+j+k))
#             if len(set(i+j+k))==3:
#                 list_result+=[int(i+j+k)]
# print("能组成%d个互不相同且无重复数字的三位数: "%len(list_result))
# print(list_result)
# pprint.pprint(list_result)

#从 00 01 10  到  11 10 10
for num in range(6,58):
    a = num >> 4 & 3
    b = num >> 2 & 3
    c = num & 3
    if( (a^b) and (b^c) and (c^a) ):
        print (a+1,b+1,c+1)







