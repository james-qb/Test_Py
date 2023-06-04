#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/6/3 10:09
  @Description:描述
  @Author  : qiubin
  @File    : 001_max_num.py
  @Software: PyCharm
"""
from collections import Counter

# num_lst = list(input())
num_lst = "54697785662154564"
cnt = Counter(num_lst)
stack = list()
used = {}

for num in num_lst:
    if used.get(num, 0) == 2:
        cnt[num] -= 1
    else:
        while len(stack) > 0 and num > stack[-1] and cnt[stack[-1]] > 2:
            cnt[stack[-1]] -= 1  # 对于栈顶弹出的元素，其计数-1
            used[stack[-1]] -= 1  # 同时在used集合中移除
            stack.pop()  # 栈顶元素弹出
        stack.append(num)
        # 对已经使用的num做统计
        if used.get(num, 0) == 0:
            used[num] = 1
        else:
            used[num] += 1

print("".join(stack))
