#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 15:37
# @Author  : qiubin
# @File    : test_weixin.py
# @Software: PyCharm
from appium import webdriver
from time import sleep


desired_caps = {
            'platformName': 'Android',
            'fastReset': 'false',
            'noReset': True,
            'platformVersion': '7.1.1',
            'deviceName': 'M95QACP58HCH6',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'fullReset': 'false',
            # 'unicodeKeyboard': 'True',
            # 'resetKeyboard': 'True',
            'chromeOptions': {
                'androidProcess': 'com.tencent.mm:tools'
                }
            }


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(5)
driver.find_element_by_android_uiautomator('text("微信")').click() #点击微信Tab


# 定义一个滑动屏幕的方法
def swipe_down(t):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = int(x * 0.5)  # x坐标
    y1 = int(y * 0.25)  # 起始y坐标
    y2 = int(y * (0.25 + t))  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, 500)


swipe_down(0.4) # 向下滑动屏幕的40%，准备从顶部进入小程序
sleep(2)
driver.find_element_by_android_uiautomator('text("xxx")').click()# 点击顶部的图标进入小程序
sleep(5)
print(driver.contexts)
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
sleep(5)
