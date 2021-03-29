#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 9:29
# @Author  : qiubin
# @File    : test_xlsx.py
# @Software: PyCharm

import openpyxl
import unittest

from ddt import ddt,data,unpack
import os
import autoit


# name_path = r"C:\Users\admin\Documents\WeChat Files\qiubin1984\FileStorage\File\2019-07\72a6e5c84419711b048d0e9930b57fe2_t.gif"
# print(os.path.splitext(os.path.basename(name_path)))

for file in os.listdir('D:/'):
    if os.path.splitext(file)[1][1:] in ['png', 'zip']:
        print(file)
autoit.run("notepad.exe")
autoit.win_wait_active("[CLASS:Notepad]", 3)
print(autoit.win_get_process("[CLASS:Notepad]"))
autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
autoit.win_close("[CLASS:Notepad]")
autoit.control_click("记事本", "[CLASS:Button;Instance:3]")
autoit.win_close("[CLASS:Notepad]")
autoit.control_click("记事本", "[CLASS:Button;Instance:2]")
