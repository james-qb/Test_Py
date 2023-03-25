#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 11:16
# @Author  : qiubin
# @File    : Test_same.py
# @Software: PyCharm
import math
import operator
from functools import reduce

from PIL import Image


def compare(pic1, pic2):
    """
    :param pic1: 图片1路径
    :param pic2: 图片2路径
    :return: 返回对比的结果
    """
    try:
        image1 = Image.open(pic1)
        image2 = Image.open(pic2)
    except (FileNotFoundError, IOError) as e:
        print(e)
    else:
        histogram1 = image1.histogram()
        histogram2 = image2.histogram()
        differ = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
        print(differ)
        return differ


compare(r'D:\360Downloads\IMG_0020.JPG', r'D:\360Downloads\IMG_0021.JPG')
