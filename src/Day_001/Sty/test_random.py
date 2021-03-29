#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 9:17
# @Author  : qiubin
# @File    : test_random.py
# @Software: PyCharm
from random import randint
lst = [randint(0, 50) for _ in range(100)]
print(lst[:5])
