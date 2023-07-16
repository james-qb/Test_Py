#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/7/16 9:57
  @Description:描述
  @Author  : qiubin 
  @File    : 009_max_sum_sublist.py
  @Software: PyCharm
"""
"""
题目描述：
给定一个数组，求出该数组和最大连续子数组
[-2, 1, -3, 4, 3, -1, 2, 1, -5, 4]

输出：
9
[4, 3, -1, 2, 1]
"""
lst = [-2, 1, -3, 4, 3, -1, 2, 1, -5, 4]


# 动态规划方法
def find_maxsum_sublist(num_lst):
    res = num_lst[0]
    sum_ = 0
    max_lst = []
    sum_lst = []
    for num in num_lst:
        if sum_ > 0:
            sum_ += num
            sum_lst.append(num)
        else:
            sum_ = num
            sum_lst = [num]
        # res = max(res, sum_)
        if sum_ > res:
            res = sum_
            max_lst = sum_lst[::]
    print(res, max_lst)
    return res


find_maxsum_sublist(lst)
