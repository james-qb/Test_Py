#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 16:03
# @Author  : qiubin
# @File    : test_baidu.py
# @Software: PyCharm


import unittest
import os
import time
from selenium import webdriver


class Baidu(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.url = 'http://uatcas.cre.com.hk/dmp-fresh-frontend'
    #     cls.driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe")
    #     cls.driver.get(cls.url)
    #     cls.driver.maximize_window()
    #     cls.driver.implicitly_wait(10)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    def setUp(self):
        self.url = 'http://uatcas.cre.com.hk/dmp-fresh-frontend'
        self.driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def test_1_login(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('chenxiaojun56')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('cxj123456')
        driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
        id_element = driver.find_element_by_xpath('//*[@id="app"]/div/ul/div[3]/div/p')
        print(driver.title)
        self.assertEqual(id_element.text, "欢迎您：水产系统管理员", msg='登录账号不正确')

    def test_2_purchase(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('chenxiaojun56')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('cxj123456')
        driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/ul/div[2]/div[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="sidebar"]/div/li[2]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//form/div[1]/div/div/input').send_keys('P20040070')
        driver.find_element_by_xpath('//form/div[1]/div/div/div/button').click()
        time.sleep(3)
        code_str = driver.find_element_by_xpath('//div[@class="list-item"][1]/div/span[2]/span[1]')
        time.sleep(2)
        self.assertEqual(code_str.text, 'P20040070', msg='不正确')
