#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 14:00
# @Author  : qiubin
# @File    : Test.py
# @Software: PyCharm

import matplotlib.pyplot as plt
from PIL import Image
import serial, os, re
import time, sys, xlsxwriter, datetime

sys.setrecursionlimit(20000)

class Xllgoinfo(object):
    def __init__(self, path=''):
        fname = path + time.strftime('%Y-%m-%d', time.gmtime())
        self.row = 0
        self.xl = xlsxwriter.Workbook(path + fname + '.xlsx')
        self.style = self.xl.add_format({'bg_color': 'red'})  # 颜色初始化
        self.styleother = self.xl.add_format({'bg_color': 'green'})

    def xl_write(self, *args):
        col = 0
        style = ' '
        if 'Pass' in args:
            style = self.styleother
        if 'Fail' in args:
            style = self.style

        for val in args:
            self.sheet.write_string(self.row, args.index(val), str(val))
        self.row += 1

    def log_init(self, sheetname, *titles):
        self.sheet = self.xl.add_worksheet(sheetname)
        self.sheet.set_column('A:E', 10)
        self.xl_write(*titles)

    def log_write(self, *args):  # 写入内容
        self.xl_write(*args)

    def log_close(self):
        self.xl.close()


path = r'D:\work_student\测试组的人员底图'
filenames = []
for files in os.listdir(path):
    if os.path.splitext(files):
        file = os.path.join(path, files)
        filenames.append(file)
filenames = filenames * 1000


def recv(serial):
    start = datetime.datetime.now()
    try:
        while True:
            time.sleep(0.5)
            data = serial.readline()
            now = datetime.datetime.now()
            # print(data)
            # print('n',now)
            timeout = (now - start).seconds
            if data == b'' and timeout < 50:
                continue
            elif timeout >= 50:
                data = 'unkown'
                break
            else:
                break
        time.sleep(0.02)
    except Exception as e:
        print(e)
        data = b''
    return data


def getserial(pid):
    times = time.ctime()
    xinfo = Xllgoinfo()
    xinfo.log_init('test', '时间', 'track_id', 'liveness', 'score', 'id', 'next_mode', 'imgname', 'result')
    ser = serial.Serial('COM3', 115200, timeout=5)

    for filename in filenames:
        img = Image.open(filename)  # 打开图片，返回PIL image对象
        img.show()
        name = os.path.splitext(os.path.basename(filename))[0]  # 输出当前图片名字
        # print('s',name)
        plt.pause(3)  # 该句显示图片3秒
        if '空白' not in str(name):
            data = recv(ser)
            if data != b'' and data != 'unknow':
                strs = data.decode('utf-8')
                track_id = (re.findall(r"track_id=(.+?),", strs))[0]
                liveness = (re.findall(r"liveness=(.+?),", strs))[0]
                score = (re.findall(r"score=(.+?),", strs))[0]
                id = (re.findall(r", id=(.+?)\)", strs))[0]
                next_mode = (re.findall(r", next_mode=(.+?)", strs))[0]
                strings = [int(track_id), float(liveness), float(score), id, next_mode]
                print(strs + times)
                print(strings)
                # now = datetime.datetime.now()
                # print(now)
                # timeout = (now - start).seconds
                if float(score) >= 0.9:
                    if str(id) == str(name):
                        # print(strs + times)
                        # print(times+strs)
                        xinfo.log_write(times, track_id, liveness, score, id, next_mode, name, 'Pass')
                    else:
                        xinfo.log_write(times, track_id, liveness, score, id, next_mode, name, 'Fail')
                else:
                    xinfo.log_write(times, track_id, liveness, score, id, next_mode, name, '识别率未达到')
            ser.flushInput()
            os.system(('taskkill /IM %s /F') % pid)
        elif data == 'unknow':
            xinfo.log_write('unknow')
        else:
            ser.flushInput()
            os.system(('taskkill /IM %s /F') % pid)
            continue
    xinfo.log_close()


if __name__ == '__main__':
    getserial("Microsoft.Photos.exe")
