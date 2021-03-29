#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 10:08
# @Author  : qiubin
# @File    : test_md5.py
# @Software: PyCharm
import hashlib


def MD5(stra):
    """

    :rtype: str
    """
    h1 = hashlib.md5()
    h1.update(stra.encode(encoding='utf-8'))
    return h1.hexdigest()  # 小写


if __name__ == "__main__":
    str_a = '123232'
    md5 = MD5(str_a)
    print("加密前为 ：" + str_a)
    print("加密后为：" + md5)
