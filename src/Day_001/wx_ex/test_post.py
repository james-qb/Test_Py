#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 14:42
# @Author  : qiubin
# @File    : test_post.py
# @Software: PyCharm
import requests

# url = "http://httpbin.org/post"
# data = {"key1": "value1", "key2": "value2"}
# headers = {"Content-type": "application/x-www-form-urlencoded"}
# r = requests.post(url=url, data=data, headers=headers)
# print(r.text)

# import requests
#
# files = {'file': open(r'D:\1.txt', 'rb')}
# url = "http://httpbin.org/post"
# fields = {"field0": "value", "field1": "value"}  # 删掉fields效果一样
# r = requests.post(url=url, data=fields, files=files)
# print(r.status_code)
# print(r.text)
#
# import requests
# url = r'http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png'
# path = 'D://2.jpg'
# r = requests.get(url=url, stream=True)
# print(r.status_code)
# with open(path, 'wb') as f:
#     f.write(r.content)
#

import requests

url = "https://www.baidu.com"

payload = {}
headers = {
  'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/69.0.3497.100 Safari/537.36",
  'Cookie': 'BIDUPSID=DFF97F4A43B1B86895D78022DE5B1C68; PSTM=1594696578; \
  BAIDUID=DFF97F4A43B1B86805C7868F3E819856:FG=1; BDSVRTM=11; BD_HOME=1; \
  H_PS_PSSID=32189_1453_31672_32139_32045_32230_31322_32298_26350_32261'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
