#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/7/15 8:49
  @Description:描述
  @Author  : qiubin 
  @File    : 007_slipt_num.py
  @Software: PyCharm
"""
"""
面试题
给定数组[2,3,4,6,7]
输出2-4,6-7
"""
num_lst = [0, 2, 3, 4, 4, 5, 6, 7, 9, 11, 12, 13, 14]
# num_lst = [1, 3]
stack = []
start = 0
stack.append(str(num_lst[0]))
flag = False
for i in range(1, len(num_lst)):
    if num_lst[i] == num_lst[i - 1] + 1:
        if i == len(num_lst) - 1:
            stack[-1] = stack[-1] + '-' + str(num_lst[i])
        flag = True
    else:
        if flag:
            stack[-1] = stack[-1] + '-' + str(num_lst[i - 1])
        stack.append(str(num_lst[i]))
        flag = False
        start = i
print(stack)
print(','.join(stack))
