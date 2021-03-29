#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 9:30
# @Author  : qiubin
# @File    : test_xw_event.py
# @Software: PyCharm
"""定义Frame窗口基类"""
import sys
import wx


class MyFrame(wx.Frame):
    session = {}  # 模拟Web的session，保留会话的数据

    def __init__(self, title, size):
        super().__init__(parent=None, title=title, size=size,
                         style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX)
        # style是定义窗口风格，具体看官网。https://docs.wxpython.org/wx.Frame.html#wx-frame
        # 上面的DEFAULT就是包含了下面所有的风格的：
        # wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER |
        # wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN
        # 上面的例子是去掉了其中的一个。官网的例子是这样的：
        # style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)  去掉了2个来固定窗口大小
        # 设置窗口居中
        self.Center()
        # 设置Frame窗口内容面板
        self.contentpanel = wx.Panel(parent=self)
        # 图标文件
        ico = wx.Icon("./f1.ico", wx.BITMAP_TYPE_ICO)
        # 设置图标
        self.SetIcon(ico)
        # 设定窗口大小，这里设置了相同的最大和最小值，也就是固定了窗口大小。
        # 因为上面的窗口风格了保留了wx.RESIZE_BORDER，所以这里用另外一个放来来保证大小不可调整
        # 这样做有一点不好，就是鼠标放在窗口边缘，会变成调整窗口大小的样子，但是拉不动窗口
        self.SetSizeHints(size, size)
        # 绑定关闭按钮的点击事件
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        # 退出系统
        self.Destroy()
        sys.exit()


"""登录窗口"""


class LoginFrame(MyFrame):
    accounts = {
        'admin': {'pwd': 'admin'},
        'root': {'pwd': '123456'},
        'user': {'pwd': 'user123'},
    }

    def __init__(self):
        super().__init__(title="用户登录", size=(340, 230))

        # 创建界面中的控件
        username_st = wx.StaticText(self.contentpanel, label="用户名：")  # 输入框前面的提示标签
        password_st = wx.StaticText(self.contentpanel, label="密码：")
        self.username_txt = wx.TextCtrl(self.contentpanel)  # 输入框
        self.password_txt = wx.TextCtrl(self.contentpanel, style=wx.TE_PASSWORD)

        # 创建FlexGrid布局对象
        fgs = wx.FlexGridSizer(2, 2, 20, 20)  # 2行2列，行间距20，列间距20
        fgs.AddMany([
            # 下面套用了3个分隔，垂直居中，水平靠右，固定的最小尺寸
            (username_st, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.FIXED_MINSIZE),
            # 位置居中，尺寸是膨胀
            (self.username_txt, 1, wx.CENTER | wx.EXPAND),
            (password_st, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.FIXED_MINSIZE),
            (self.password_txt, 1, wx.CENTER | wx.EXPAND),
        ])
        # 设置FlexGrid布局对象
        fgs.AddGrowableRow(0, 1)  # 第一个0是指第一行，权重1
        fgs.AddGrowableRow(1, 1)  # 第一个1是指第二行，权重也是1
        # 上面一共就2行，用户名和密码，就是2行的空间是一样的
        fgs.AddGrowableCol(0, 1)  # 第一列，权重1，就是标签的内容
        fgs.AddGrowableCol(1, 4)  # 第二列，权重4，就是输入框，并且输入框是膨胀的应该会撑满
        # 上面2列分成5分，第一列占1/5，第二列占4/5

        # 创建按钮对象
        ok_btn = wx.Button(parent=self.contentpanel, label="确定")
        cancel_btn = wx.Button(parent=self.contentpanel, label="取消")
        # 绑定按钮事件：事件类型，绑定的事件，绑定的按钮
        self.Bind(wx.EVT_BUTTON, self.ok_btn_onclick, ok_btn)
        self.Bind(wx.EVT_BUTTON, self.cancel_btn_onclick, cancel_btn)

        # 创建水平Box布局对象，放上面的2个按钮
        box_btn = wx.BoxSizer(wx.HORIZONTAL)
        # 添加按钮控件：居中，四周都有边框，膨胀。border是设置边框的大小，实际效果没有框，但是占用空间
        box_btn.Add(ok_btn, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        box_btn.Add(cancel_btn, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=10)

        # 创建垂直Box，把上面的fgs对象和box_btn对象都放进来
        box_outer = wx.BoxSizer(wx.VERTICAL)
        box_outer.Add(fgs, -1, wx.CENTER | wx.ALL | wx.EXPAND, border=25)  # 权重是-1，就是不指定了
        # (wx.ALL ^ wx.TOP)这里只加3面的边框，上面就不加了
        box_outer.Add(box_btn, -1, wx.CENTER | (wx.ALL ^ wx.TOP) | wx.EXPAND, border=20)

        # 上面全部设置完成了，下面是设置Frame窗口内容面板
        self.contentpanel.SetSizer(box_outer)  # self.contentpanel 是在父类里定义的

    def ok_btn_onclick(self, event):
        username = self.username_txt.GetValue()  # 取出输入框的值
        password = self.password_txt.GetValue()
        if username in self.accounts:
            if self.accounts[username].get('pwd') == password:
                self.session['username'] = username
                print("登录成功")
                # 接下来要进入下一个Frame
                msg = "用户密码正确"
                dialog = wx.MessageDialog(self, msg, "登录失败")
                dialog.ShowModal()  # 显示对话框
                dialog.Destroy()
                return
            else:
                msg = "用户名或密码错误"
        else:
            msg = "用户名不存在"
        print(msg)
        dialog = wx.MessageDialog(self, msg, "登录失败")  # 创建对话框
        dialog.ShowModal()  # 显示对话框
        dialog.Destroy()  # 销毁对话框

    def cancel_btn_onclick(self, event):
        self.on_close(event)


app = wx.App()
lg = LoginFrame()
lg.Show()
app.MainLoop()