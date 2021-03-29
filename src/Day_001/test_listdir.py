#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 16:56
# @Author  : qiubin
# @File    : test_listdir.py
# @Software: PyCharm
import datetime
import os


def sortfile(path):
    """
    获取path目录下，最后更新的文件名称
    """

    fl = os.listdir(path)  # 获取path目录文件列表
    # 时间戳进行倒序排序
    print(fl)
    fl.sort(key=lambda fn: os.path.getmtime(path + fn) if not os.path.isdir(path + fn) else 0)
    # date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象
    print(fl)
    print(os.path.getmtime(path + fl[-1]))
    dt = datetime.datetime.fromtimestamp(os.path.getmtime(path + fl[-1]))
    print(dt)
    # dt.strftime("%Y年%m月%d日 %H时%M分%S秒" 将date对象格式化显示
    print('最后改动的文件是: ' + fl[-1] + "，时间：" + dt.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日',
                                                                                                 h='时', f='分', s='秒'))
    msg = "自动化测试完成，点击下面链接查看测试结果：\n " + "http://192.168.200.8/result/" + str(dt) + "/" + fl[-1]
    return msg


if __name__ == '__main__':
    sortfile('D:/')
    ll = map(lambda x: x if x > 1 else 1, [1, 0.9, 8, 1])
    print(list(ll))
