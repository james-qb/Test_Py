#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/6/5 22:31
  @Description:描述
  @Author  : qiubin 
  @File    : 012_fama_weight.py
  @Software: PyCharm
"""
# n = 6
# weights = list(map(int, '1 2 5 10 20 50'.strip().split(' ')))
# nums = list(map(int, '6 6 5 5 3 6'.strip().split(' ')))
# sums = 0
# print(nums, weights)
# for i in range(n):
#     sums += (nums[i] * weights[i])
# print(sums)
# arr = [0] * (sums + 1)
# arr[0] = 1
# print(arr)
# for i in range(n):
#     for j in range(nums[i]):
#         pass
"""
你有一架天平和 N 个砝码，这 N 个砝码重量依次是 W1,W2,⋅⋅⋅,WN。
请你计算一共可以称出多少种不同的正整数重量？
注意砝码可以放在天平两边。
输入格式
输入的第一行包含一个整数 N。
第二行包含 N 个整数：W1,W2,W3,⋅⋅⋅,WN。
输出格式
输出一个整数代表答案。
"""
w_num = 6
w_lst = list(map(int, '1 2 7 10 20 50'.strip().split(' ')))

# w_num = 3
# w_lst = list(map(int, '1 4 6'.strip().split(' ')))

w_sum = sum(w_lst)
# wdp = [[0] * (w_sum + 1) for _ in range(w_num + 1)]
# wdp[0][0] = 1
# for i in range(1, w_num + 1):
#     for j in range(w_sum + 1):
#         if wdp[i - 1][j]:
#             wdp[i][j] = 1
#             wdp[i][j + w_lst[i - 1]] = 1
#             wdp[i][abs(j - w_lst[i - 1])] = 1
# print(wdp)
# 方法二：优化版节省空间,采用临时tmp_dp,记录上次的结果
dp = [0 for _ in range(w_sum + 1)]
dp[0] = 1
tmp_dp = dp[::]
for i in range(0, w_num):
    for j in range(w_sum, -1, -1):
        if tmp_dp[j] == 1:
            dp[j] = dp[abs(j - w_lst[i])] = dp[j + w_lst[i]] = 1
    tmp_dp = dp[::]
print(dp)
# 方法三：暴力破解
sum_set = set()
for num in w_lst:
    tmp_set = {num}
    for tmp in sum_set:
        tmp_set.add(tmp + num)
        tmp_set.add(abs(tmp - num))
    sum_set |= tmp_set
print(sum_set)
# 递归法
v = [0] * (w_sum + 1)

count = 0


def dfs(sum_, i):
    global count
    count += 1
    v[sum_] = 1
    if i == len(w_lst):
        return None
    dfs(sum_ + w_lst[i], i + 1)
    dfs(sum_, i + 1)
    dfs(abs(sum_ - w_lst[i]), i + 1)


dfs(0, 0)
print(v)
print(count)
