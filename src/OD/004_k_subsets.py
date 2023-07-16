#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/6/11 16:36
  @Description:描述
  @Author  : qiubin 
  @File    : 004_k_subsets.py
  @Software: PyCharm
"""
k = 6
num_list = [5, 2, 1, 5, 2, 1, 5, 1, 1, 1, 4]

num_list.sort()
print(num_list)


def can_divide(num_list, k):
    tatol = sum(num_list)
    if tatol % k != 0:
        return False

    target = int(tatol / k)
    num_list.sort()
    if num_list[-1] > target:
        return False
    n = len(num_list)
    dp = [False] * n
    cur_sum = [0] * n
    dp[0] = True
    for i in range(n):
        if not dp[i]:
            continue
        for j in range(n):
            if cur_sum[i] + num_list[j] > target:
                break
            if j > 0:
                next_ = j
                if not dp[next_]:
                    cur_sum[next_] = (cur_sum[i] + num_list[j]) % target
                    print(dp[n - 1], cur_sum)
                    dp[next_] = True

    print(dp)
    return dp[n - 1]


can_divide(num_list, k)
