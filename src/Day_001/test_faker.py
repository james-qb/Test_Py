#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2021/11/7 22:10
  @Description:描述
  @Author  : qiubin 
  @File    : test_faker.py
  @Software: PyCharm
"""
from faker import Faker

f = Faker(locale='zh_CN')
for i in range(5):
    print(f.name() + ":" + f.address() + ":" + f.ssn())
