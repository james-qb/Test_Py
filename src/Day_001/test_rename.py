#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 10:17
# @Author  : qiubin
# @File    : test_rename.py
# @Software: PyCharm
import os
os.chdir(r"D:\BaiduNetdiskDownload\Java快速入门教程视频\day10")
file_dir = os.getcwd()

temp_dir = os.getcwd().split("\\")[-1]
print(file_dir, temp_dir)

for filename in os.listdir(file_dir):
    ll = filename.replace('day01', temp_dir)
    print(ll)
    if not filename.startswith(temp_dir):
        print(os.path.join(file_dir, filename), os.path.join(file_dir, ll))
        os.rename(os.path.join(file_dir, filename), os.path.join(file_dir, ll))
