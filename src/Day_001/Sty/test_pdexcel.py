#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2021/12/19 18:31
  @Description:描述
  @Author  : qiubin 
  @File    : test_pdexcel.py
  @Software: PyCharm
"""
import pandas as pd

# 写
dic1 = {'标题列1': ['张三', '李四'],
        '标题列2': [80, 90]
        }
df = pd.DataFrame(dic1)
df.to_excel('D:\\1.xlsx', index=False)
