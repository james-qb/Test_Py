#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 15:31
# @Author  : qiubin
# @File    : test_app.py
# @Software: PyCharm


from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    # 用真机的时候，这个参数deviceName没什么用，但是还是必须要有这个参数，值的话随便填就行了
    'deviceName': 'emulator-5554',
    'platformVersion': '7.1.1',
    'appPackage': 'com.tencent.mtt.x86',
    'appActivity': 'com.tencent.mtt.x86.SplashActivity',
    'noReset': True,
    'unicodeKeyyboard': True,
    'resetKeyboard': True,
    'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},

}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(60)
driver.quit()
