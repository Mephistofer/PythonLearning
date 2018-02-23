#!/usr/bin/env python 
# -*- coding: utf-8 -*
'''
Created on 2017年9月19日

@author: Saya
'''
# from lib2to3.fixer_util import Number
# import profile
bicycles = [' trek ', 'cannondale', 'cat', 'redline', 'cat', 'Apecialized']
bicycles[1] = bicycles[1].title()
bicycles.insert(0, "d")
bicycles.insert(2, "ffff")
bicycles[1] = bicycles[1].title().strip()
print("初始", bicycles)
bicycles.reverse()
print("反序", bicycles)
bicycles.sort()
print("顺序",bicycles)
bicycles.sort(reverse=True)
print("逆序", bicycles)

del bicycles[3]
print("当前", bicycles)
out = bicycles.pop()
print("pop",out)
print("当前", bicycles)
out = bicycles.pop(0)
print("pop(0)",out)
print("当前", bicycles)
while 'cat' in bicycles:
    bicycles.remove('cat')

print("当前", bicycles)
print("顺序", sorted(bicycles))
print("逆序", sorted(bicycles, reverse=True))
print("当前", bicycles)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())
    print("I can't wait to see your next trick, %s."%magician.title())
    print('%o, %x, %x, %X' % (64, 64, 255, 255))

for value in range(1, 6):    
    print(value)
    value = value**3
    print(value)
    
    
numbers = list(range(1,6,2))
print(numbers)

numbers = range(1,6)
print(numbers)
        
''' 
列表解析 
要使用这种语法，首先指定一个描述性的列表名，如squares ；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式
为value**2 ，它计算平方值。接下来，编写一个for 循环，用于给表达式提供值，再加上右方括号。
在这个示例中，for 循环为for value in range(1,11) ，它将值1~10提供给表达式value**2 。请注意，这里的for 语句末尾没有冒号
'''
squares = [value**2 for value in range(1,11)]
print(squares)

list_num = (1,2,3,4)
d = [i*100 + j*10 + k for i in list_num for j in list_num for k in list_num if (i != j and j != k and k!= i)] 
print ("总数量：", len(d), d)

d = []
list_num = (1,2,3,4)
for i in list_num: 
    for j in list_num: 
        for k in list_num[0:4]: 
            if (i != j and j != k and k!= i):                
                d.append(i*100 + j*10 + k) 
print ("总数量：", len(d), d[:29])


p = d[:]    # 赋值
q = d       # 引用

d.append(8799)

print(p)
print(q)

dimensions = (200, 50)
use = 200
# dimensions[0] = 250 #not invalid
if use in dimensions:
    print(use)

car = "KkK"
print(car.upper() == "KKK")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

dict1 = {}
dict2={1,2,1} #set
dict1["color"] = "yellow"
dict1["point"] = 9
dict1["color"] = "green"

dict1.setdefault('a', []).append(1)

del dict1["point"]
print(dict1)
print (dict2)

bob1 = dict( job='dev',name='Bob', age=40)
print(bob1)
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5
    }
print(rec)

for a1,a2 in rec.items():
    print(a1,a2)
    
for a2 in bob1.values():
    if a2 == 40:
        print(a2,"---")
        
for a1 in sorted(bob1): #和语句 ‘for a1 in sorted(bob1.keys()):’ 一样
   print(a1)  
       
for a1 in bob1.keys():
    if a1 == "job":
        print(bob1[a1], '---')

print("Sarah's favorite language is " +
      dict1['color'].title() +
      ".")

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key.title())
    print("Value: " + value)
    
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

def greet_user():
    """显示简单的问候语"""
    print("Hello!")
    
greet_user()

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics',
aa = '9')
print(user_profile)

a = "ABC"
b = a
a = "XYZ"
print(b)

# import MyFun
# MyFun.make_pizza(4)

# from MyFun import make_pizza
# make_pizza(8)

# from MyFun import make_pizza as makePizza
# makePizza(8)

# from MyFun import *
# make_pizza(8)

import MyFun
myDog=MyFun.Dog("hello", 6)
myDog.roll_over()

MyFun.make_pizza(2)
MyFun.describe_pet("wo")

# from MyFun import Dog
# myDog=Dog("hello", 6)
# myDog.roll_over()

# import os
# os.system("pause")



