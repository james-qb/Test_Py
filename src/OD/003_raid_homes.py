#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/6/10 11:30
  @Description:描述
  @Author  : qiubin 
  @File    : 003_raid_homes.py
  @Software: PyCharm
"""
import random
import time

num_lst = []
for i in range(10000):
    num_lst.append(random.randint(0, 10))
num_lst = [2, 9, 7, 1, 3, 4]
t1 = time.time()
f_i_1 = f_i_2 = 0
# 这种跳格问题，变量赋值时，要正确的前移传递
for i, x in enumerate(num_lst):
    f_i_2, f_i_1 = f_i_1, f_i_2 + num_lst[i]
t2 = time.time()
print(t2 - t1)
print(max(f_i_1, f_i_2))
