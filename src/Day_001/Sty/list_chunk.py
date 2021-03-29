#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 11:05
# @Author  : qiubin
# @File    : list_chunk.py
# @Software: PyCharm
from math import ceil


def chunk(lst, size):
    if size <= 0:
        return lst
    else:
        # for i in range(0, ceil(len(lst)/size)):
        #     print(lst[i*size:i*size+size])
        # return [lst[i*size:i*size+size] for i in range(0, ceil(len(lst)/size))]
        return list(map(lambda x: lst[x*size:x*size+size], list(range(0, ceil(len(lst)/size)))))


print(chunk([1, 2, 3, 4, 5], 1))
