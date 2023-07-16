#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/7/16 11:04
  @Description:描述
  @Author  : qiubin 
  @File    : 010_flat_list.py
  @Software: PyCharm
"""

"""
已知如下数组，编写一个程序将数组扁平化去并除其中重复部分数据，最终得到一个升序且不重复的数组
"""
lst = [
    [1, 2, 2],
    [3, 4, 5, 5],
    [6, 7, 8, 9, [11, 12, [12, 13, [14]]]], 10
]


# 通过+的特性进行列表的展开
def flat_lst(num_lst):
    sum_ = []
    for i in range(len(num_lst)):
        if isinstance(num_lst[i], list):
            sum_ += flat_lst(num_lst[i])
        else:
            sum_.append(num_lst[i])
    return sum_


out_lst = flat_lst(lst)
res_a = list(set(out_lst))
res_a.sort(key=out_lst.index)
print(res_a)

# res = list(set(flat_lst(lst)))
#
# print(list(set(res)).sort())
