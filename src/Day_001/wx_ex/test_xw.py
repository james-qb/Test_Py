#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 9:16
# @Author  : qiubin
# @File    : test_xw.py
# @Software: PyCharm
import wx
import time
import wx
import sys


def openfile(event):  # 定义打开文件事件
    path = path_text.GetValue()
    with open(path, "r", encoding="utf-8") as f:  # encoding参数是为了在打开文件时将编码转为utf8
        content_text.SetValue(f.read())


def closewindows(event):
    frame.Destroy()
    sys.exit(0)


app = wx.App()
frame = wx.Frame(None, title="文件打开", pos=(1000, 200), size=(500, 400))

path_text = wx.TextCtrl(frame, pos=(5, 5), size=(350, 24))
open_button = wx.Button(frame, label="打开", pos=(370, 5), size=(50, 24))
open_button.Bind(wx.EVT_BUTTON, openfile)  # 绑定打开文件事件到open_button按钮上

save_button = wx.Button(frame, label="保存", pos=(430, 5), size=(50, 24))

content_text = wx.TextCtrl(frame, pos=(5, 39), size=(475, 300), style=wx.TE_MULTILINE)
#  wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行

frame.Show()
frame.Bind(wx.EVT_CLOSE, closewindows)
app.MainLoop()

