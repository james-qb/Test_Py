#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 10:20
# @Author  : qiubin
# @File    : max_pairs.py
# @Software: PyCharm


def max_pairs(dic):
    if len(dic) == 0:
        return dic
    max_val = max(dic, key=dic.get)
    print(max_val)
    return {k: dic[k] for k in dic.keys() if dic[k] == max(dic.values())}
    # resp = []
    # for item_a in dic.items:
    #     if item_a[1] == max_val:
    #         resp.append(item_a)


temp_dic = {'a': 10, 'b': 15, 'c': -1, 'd': 15}
print(max_pairs(temp_dic))

