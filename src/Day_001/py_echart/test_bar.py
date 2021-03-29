#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 16:51
# @Author  : qiubin
# @File    : test_bar.py
# @Software: PyCharm
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

# 示例数据
cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data1 = [123, 153, 89, 107, 98, 23]
data2 = [56, 77, 93, 68, 45, 67]

"""
主题设置：
默认white
"""
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
bar.add_xaxis(cate)
bar.add_yaxis('电商渠道', data1)
bar.add_yaxis('门店', data2)
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                    markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"),
                                                            opts.MarkPointItem(type_="min", name="最小值", symbol="rect")]))
bar.set_global_opts(title_opts=opts.TitleOpts(title="Theme-ROMANTIC"))


bar.render('./pic.html')
