#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 17:54
# @Author  : qiubin
# @File    : test_moudle.py
# @Software: PyCharm
from collections import namedtuple, deque

person = namedtuple('person', ['name', 'sex', 'age'])
print(type(person))
c = person('Matin', 'male', 25)
a = person(name='Jacke', sex='male', age=18)
print(type(a))
b = a.name, a.sex, a.age
print(a, c)


str="alex like pig"
dic = {}
for el in str:
    if el:
        dic[el] = dic.setdefault(el, 0)+1
print(dic)


temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
dp = deque(temp)
print(dir(dp))
dp.rotate(5)
print(dp)
sd = [x**3for x in dp]
print(sd)

temp.reverse()
print(temp)
cc = list()
print(cc)