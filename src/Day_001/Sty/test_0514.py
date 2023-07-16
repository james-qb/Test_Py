#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/5/14 16:02
  @Description:描述
  @Author  : qiubin 
  @File    : test_0514.py
  @Software: PyCharm
"""
import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})
ff = df.set_index('name', inplace=False)
print(ff
      )
