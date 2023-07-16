#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/6/14 22:04
  @Description:描述
  @Author  : qiubin 
  @File    : 005_work_reward.py
  @Software: PyCharm
"""
import time

n = 10
work_time = 50
nums_lst = [[20, 20], [20, 10], [20, 5], [30, 25], [10, 10], [10, 9], [9, 8], [5, 5], [6, 3], [1, 1]]
res = 0


# 通过回溯的方法求解
def max_reward(left_time, cur_reward, index, nums_list, contaier=None):
    global res
    if contaier is None:
        contaier = []
    if left_time == 0 or index == n:
        print(cur_reward, contaier[::])
        res = max(res, cur_reward)
        return None
    else:
        for i in range(index, n):
            # print(left_time, cur_reward)
            if left_time >= nums_list[i][0]:
                contaier.append(nums_list[i])
                max_reward(left_time - nums_list[i][0], cur_reward + nums_list[i][1], i + 1, nums_list, contaier)
                contaier.pop()
            else:
                continue


t1 = time.time()
result = {}
nums_lst.sort(key=lambda x: (x[0], -x[1]))
print(nums_lst)
max_reward(work_time, 0, 0, nums_lst)
print(res)
t2 = time.time()
print("0.10%f" % (t2 - t1))
