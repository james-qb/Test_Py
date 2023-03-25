#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/3/4 10:27
  @Description:描述
  @Author  : qiubin 
  @File    : test_scan_dir.py
  @Software: PyCharm
"""
import os


def fitter_dir_find_file(obj_dir, key_wd: object = None, resultl=[]):
    for entry in os.scandir(obj_dir):
        if entry.is_dir() and entry.name not in ['System Volume Information', '$RECYCLE.BIN']:
            fitter_dir_find_file(entry.path)
        else:
            if '性能' in entry.name or 'jmeter' in entry.name:
                resultl.append(entry.path)


ll = fitter_dir_find_file
print(ll)
print(dir(ll))
print(ll.__code__)
print(ll.__defaults__)

# ll = fitter_dir_find_file('D:\\')
# print(ll)
