#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/7/1 23:09
  @Description:描述
  @Author  : qiubin 
  @File    : 006_kmp_match.py
  @Software: PyCharm
"""


def next_idx(s_lst):
    next_lst = [-1]
    i = 0
    p_len = -1
    while i < len(s_lst):
        if p_len == -1 or s_lst[p_len] == s_lst[i]:
            next_lst.append(p_len + 1)
            i += 1
            p_len += 1
        else:
            p_len = next_lst[p_len]
    print(next_lst)
    return next_lst


def next_idx_1(s_lst):
    next_lst = [0] * len(s_lst)
    i = 0
    next_lst[0] = -1
    p_len = -1
    while i < len(s_lst) - 1:
        if p_len == -1 or s_lst[p_len] == s_lst[i]:
            if s_lst[p_len + 1] == s_lst[i + 1]:
                next_lst[i + 1] = next_lst[p_len + 1]
            else:
                next_lst[i + 1] = p_len + 1
            i += 1
            p_len += 1
        else:
            p_len = next_lst[p_len]
    print(next_lst)
    return next_lst


str_ = "aaaaaabaabcac"
next_idx_1(str_)
