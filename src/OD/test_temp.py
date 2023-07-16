#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/7/4 21:55
  @Description:描述
  @Author  : qiubin 
  @File    : test_temp.py
  @Software: PyCharm
"""
# 合并集合的方法
str_list = [{'t'}, {'a', 'b'}, {'c', 'd'}, {'e', 'f'}, {'f', 'g'}, {'z', 'y'}, {'f', 'd'},
            {'d', 'b'}, {'n', 'm'}, {'m', 'l'}, {'c', 'z'}, {'f', 'p'}, {'p', 'h'}]

# 转化为set,可以减小时间复杂度,合并一个后就重新扫
pool = set(map(frozenset, str_list))
result_lst = []
while pool:
    result_lst.append(set(pool.pop()))
    while True:
        for tmp_set in pool:
            new_set = set(tmp_set)
            if result_lst[-1] & new_set:
                result_lst[-1] |= new_set
                pool.remove(tmp_set)
                break
        else:
            break
print(result_lst)
