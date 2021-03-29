#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 15:36
# @Author  : qiubin
# @File    : test_psutil.py
# @Software: PyCharm
import psutil
import random
import string

temp_list = []
for i in range(11):
    temp_list.append(''.join(random.sample(string.ascii_lowercase, 5)))
print(temp_list)
for n in range(len(temp_list)):
    temp_list[n] = '21312'
print(temp_list)
print(string.ascii_lowercase)
print(string.punctuation)
print(type(string.ascii_lowercase))

# random.shuffle(a)
#
# print(a)

# cpu_info = psutil.cpu_times()
# cpu_user = cpu_info.user
# print(cpu_user)
# print(psutil.cpu_count(logical=False))
# print(psutil.cpu_percent(1))