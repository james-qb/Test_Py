#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2022/8/10 22:16
  @Description:描述
  @Author  : qiubin 
  @File    : clac_num.py
  @Software: PyCharm
"""
import copy

# import random
#
# for i in range(100):
#     print(str(random.randint(100, 999))
#           + '  +   ' +
#           str(random.randint(100, 999)) + '  =   (    )'
#           )

a = {"x": [1, 2, 3, 4], "y": 123}
b = copy.copy(a)
print(id(a), id(b))
a["y"] = 234
a["x"][0] = 3
print(a, b)


def func_c():
    yield 1
    yield 2


x = func_c()
print(next(x))
print(next(x))

ll = 122324534543

lv = copy.deepcopy(ll)
print(id(ll), id(lv))
