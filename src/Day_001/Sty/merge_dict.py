#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 10:02
# @Author  : qiubin
# @File    : merge_dict.py
# @Software: PyCharm


def merge_dict(dic1, dic2):
    return {**dic1, **dic2}


def merge_dict_temp(dic1, dic2):
    c = dic1.copy()
    c.update(dic2)
    return c

a = {}
merge_dict()