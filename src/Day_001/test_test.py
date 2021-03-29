#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 17:55
# @Author  : qiubin
# @File    : test_test.py
# @Software: PyCharm
import json
import requests
from collections import Iterable
import numpy as np
import json
#     [1, 2], [2, 3], [3, 4], [4, 5]
# ]
# print(*a_list)
# print(list(zip(*a_list)))
#
# a = [1, 2, 3, 4, 5, 6]
# # print(list(zip(*a)))
# for i in range(10):
#     for j in range(10):
#         if i+j > 5:
#             print(i, j)
#             break

# fp = json.loads('D://FeHelper.json')
# print(type(fp))
req = {"REQUEST": {"API_ATTRS": {"Partner_ID": "10000000", "App_Sub_ID": "1000000171YA", "Sys_ID": "10000001",
                                 "App_Token": "b4d2aab1469b424c847ef1d57fb07438", "Api_ID": "cre.cresys.perm.userLogin",
                                 "Api_Version": "1.0.0", "Time_Stamp": "2019-11-22 14:13:44", "User_Token": "",
                                 "Sign": "5FA73F050816512632F2F448A85EC63F"},
                   "REQUEST_DATA": {"loginName": "chenxiaojun56", "plainPassword": "5442a4e89ae495725bf524557973cc62"}}}

# fp = open(r'D:\FeHelper.json', 'r', encoding='utf-8')
# json_fp = json.load(fp)
# print(json_fp)
url = 'https://apiuat.cresz.com.cn/openapi/?model=rs'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8"
}
# data = '{"model": "rs"}'
res = requests.request('POST', url, json=req, headers=header)
print(res.url)
print(res.status_code)
print(type(res.json()))
print(res.json())
print(type(json.dumps(res.json())))


def flatten(input_arr, out_arr=None):
    if out_arr is None:
        out_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):
            flatten(ele, out_arr)
        else:
            out_arr.append(ele)
    return out_arr


temp_list = [[1, 2, [3, 4]], [[5, 6], [7, 8]], [[9, [10, [11]]]]]



print(flatten(temp_list))

b = np.array([[1, 2, [3, 4]], [[5, 6], [7, 8]], [[9, [10, [11]]]]])
print(b)
b.flatten()
print(b)
print(dir(int))
a = 111111
print(a.bit_length())
