#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 10:17
# @Author  : qiubin
# @File    : test_rename.py
# @Software: PyCharm


# os.rename(os.path.join(file_dir, filename), os.path.join(file_dir, ll))
import os

try:
    from os import scandir
except ImportError:
    from scandir import scandir  # use scandir PyPI module on Python < 3.5


def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)  # see below for Python 2.x
        else:
            yield entry


if __name__ == '__main__':
    # import sys
    #
    # for entry in scantree(sys.argv[1] if len(sys.argv) > 1 else '.'):
    #     print(entry.path)
    # os.chdir(r"")
    # file_dir = os.getcwd()
    # # print(os.listdir(file_dir))
    # temp_dir = os.getcwd().split("\\")[-1]
    # print(file_dir, os.path.dirname(file_dir))
    # #
    # for filename in os.scandir(file_dir):
    #     ll = filename
    #     print(ll)
    file_name = r"C:\Python38\Lib\site-packages\isort-5.7.0.dist-info"
    i = 0
    while True:
        cur_name = file_name
        file_name = os.path.dirname(file_name)
        print(cur_name, file_name)
        if file_name == 'C:\Python38' or cur_name == file_name:
            break
        i += 1
    n = m = [3]
    n += m

    l = [3]
    l = l + l
    print(n, m, l)

    x = [1, 2]
    x.extend(x)
    print(x)
