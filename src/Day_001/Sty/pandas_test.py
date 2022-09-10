#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2022/4/5 13:19
  @Description:描述
  @Author  : qiubin 
  @File    : pandas_test.py
  @Software: PyCharm
"""
import numpy as np
import pandas as pd

arr = np.array(
    [
        ("Lemon", "长沙", 80, 90),
        ("James", "上海", 90, 88),
        ("Peter", "广州", 70, 50)
    ]
)

df = pd.DataFrame(arr, columns=["name", "address", "math", "chem"]
                  )
print(df)
print(df.index)
print(df.columns)
print(df.dtypes)
