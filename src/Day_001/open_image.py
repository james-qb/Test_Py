#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 9:43
# @Author  : qiubin
# @File    : open_image.py
# @Software: PyCharm
from PIL import Image
from time import sleep

try:
    im = Image.open(r'D:\1.png')
    im.show()
    sleep(3)
    im.close()
except FileNotFoundError as e:
    print("文字不存在！" + e)


from PIL import Image
import matplotlib.pyplot as plt
# img = Image.open(r'D:\1.png')
# # plt.figure("dog")
# plt.imshow(img)
# plt.show()
# plt.pause(3)
# # 关闭当前显示的图像
# plt.close()
