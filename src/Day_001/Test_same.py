#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 11:16
# @Author  : qiubin
# @File    : Test_same.py
# @Software: PyCharm
from functools import reduce
from PIL import Image
import math
import operator


def compare(pic1, pic2):
    """
    :param pic1: 图片1路径
    :param pic2: 图片2路径
    :return: 返回对比的结果
    """
    image1 = Image.open(pic1)
    image2 = Image.open(pic2)

    histogram1 = image1.histogram()
    histogram2 = image2.histogram()

    differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a-b)**2, histogram1, histogram2)))/len(histogram1))

    print(differ)
    return differ


compare(r'D:\1_1.png', r'D:\1_3.png')
