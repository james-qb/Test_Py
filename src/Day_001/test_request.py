#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 8:38
# @Author  : qiubin
# @File    : test_request.py
# @Software: PyCharm
import requests

url = 'http://devcas.cre.com.hk/osp-permission-api/user/login'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/69.0.3497.100 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8"
}

data = {
    "loginName": "msg001",
    "plainPassword": "d8ac56bd142e8918fdbef7787d3082b7",
    "applicationId": "7ef676247d134ad38c1b5281f1243f43"
}

new_dict = {}


def get_key_value(temp_dict, re_dict):
    for skey, svalue in temp_dict.items():
        if type(svalue) != dict:
            new_dict[skey] = svalue
            print(skey + ': ' + str(svalue))
        else:
            get_key_value(svalue, new_dict)
    return re_dict


req = requests.post(url, headers=header, json=data)
return_code = req.status_code
return_json = req.json()
ll = get_key_value(return_json, new_dict)
print(ll)



# print(return_code)
# print(type(return_json))
# print(return_json['msg'])
# print(type(req.headers))
