#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 12:23
# @Author  : qiubin
# @File    : gethtmltopdf.py
# @Software: PyCharm
import os
import requests
from requests import RequestException
from bs4 import BeautifulSoup
import re
import pdfkit

CURRENT_FILE_PATH = os.path.dirname(os.path.abspath('__file__'))


workdir = 'D:/Html2PDF'
url = 'https://www.zhihu.com/api/v4/columns/c_1184087344080195584/items'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

cookie = '_zap=7d62daff-1984-4a43-b799-e4046aba28ab; d_c0="AAAZJEoUZxGPTuAspqlMiIWq7RdZnT-TtOI=|1591755307";' \
         '_ga=GA1.2.31086383.1593669470; q_c1=0258114e7f1c42c3a3700fd67833b65a|1594869340000|1591843291000; ' \
         '_xsrf=ca9c778b-bb26-479c-881a-2509e84dbd4a; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1597028962,1597052764,' \
         '1597807985,1597815600; capsion_ticket="2|1:0|10:1597815603|14:' \
         'capsion_ticket|44:ODc1YjhjNTcyNTkzNGFkMWE2ZDZkMmJmODQ3Zjc2Njk=|' \
         '9b47aff7204be4f9ebad883365b32cadf6d88fb682bbdf87f808c21b010435cc"; ' \
         'KLBRSID=af132c66e9ed2b57686ff5c489976b91|1597815954|1597815138; ' \
         'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1597816005'

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'User-Agent': user_agent,
    'cookie': cookie
}


#  获取知乎专题文章标题及地址
def get_article_url(url, header):

    aircle_list = []
    while True:
        try:
            resp = requests.get(url, headers=header)
        except RequestException as error:
            print('get data error', error)
        else:
            if resp.status_code != 200:
                print('get data status_code error')
                break
            else:
                print(resp.text)
                rep_items = resp.json()
                data = rep_items['data']
                print(data)
                for aircle in data:
                    aircle_info = aircle['title'], 'https://zhuanlan.zhihu.com/p/'+str(aircle['id'])
                    aircle_list.append(aircle_info)
            paging = rep_items.get('paging')
            if paging['is_end']:
                break
            else:
                url = paging['next']
                url = url.replace('zhuanlan.zhihu.com', 'zhuanlan.zhihu.com/api')
    aircle_list = aircle_list[::-1]
    print(aircle_list)
    return aircle_list


def save_data_html(array_list, headers):
    index = 1
    os.chdir(workdir)
    for item in array_list:
        url = item[1]
        name = f'{index:03}' + '-' + item[0]
        while '/' in name:
            name = name.replace('/', '')
        html = requests.get(url, headers=headers).text

        soup = BeautifulSoup(html, 'lxml')
        content = soup.prettify()
        # content = soup.find(class_='Post-Main Post-NormalMain').prettify()
        content = soup.find(class_='Post-RichTextContainer').prettify()
        print(content)
        content = content.replace('data-actual', '')
        content = content.replace('h1>', 'h2>')
        content = re.sub(r'<noscript>.*?</noscript>', '', content)
        content = re.sub(r'src="data:image.*?"', '', content)
        #content = '<!DOCTYPE html><html><head><meta charset="utf-8"></head><h1>%s</h1><body>%s</body></html>' % (name, content)
        content = """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>{title}</title>
                    </head>
                    <body style="max-width:700px;margin: 0 auto;background-color:#fff!important;">
                    <article class="Post-Main Post-NormalMain">
                        <header class="Post-Header">
                            <h1 class="Post-Title" style="font-size: 22px;line-height: 1.4;margin-bottom: 14px;">{title}</h1>
                        </header>
                        {content}
                    </article>
                    </body>
                    <style type="text/css">
                        body{{
                            background-color:#fff;
                        }}
                    </style>

                    


                    <style type="text/css">
                        .md-toc {{
                            position: fixed;
                            height: 100%;
                            left: 0;
                            top: 0;
                            bottom: 0;
                            margin-left: 10em;
                            overflow: scroll;
                            border-bottom: 1px solid rgb(221, 221, 216);
                            box-sizing: border-box;
                            padding: 0px 20px 20px 0px;
                            width: 25em;
                        }}
                    </style>
                    </html>
                """.format(title=name, content=content)
        print(content)
        with open('%s.html' % name, 'w', encoding='utf-8') as f:
            f.write(content)
        index += 1


def cover_html_to_pdf():
    os.chdir(workdir)
    curdir = os.getcwd()
    file_list = os.listdir(curdir)
    print(file_list)
    all_html_list = []
    for path in file_list:
        file_extension = os.path.splitext(path)[1]
        if file_extension == '.html':
            all_html_list.append(path)
    all_html_list.sort()
    print(all_html_list)

    pdfkit.from_file(all_html_list, 'zhihu.pdf')


def get_content(url, data=None):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }

    req = requests.get(url, headers=header)
    req.encoding = 'utf-8'
    print(req.text)
    bs = BeautifulSoup(req.text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body  # 获取body部分
    return body


if not os.path.exists(workdir):
    os.makedirs(workdir)

a_list = get_article_url('https://www.zhihu.com/api/v4/columns/c_1184087344080195584/items', header)
save_data_html(a_list, header)
# cover_html_to_pdf()
