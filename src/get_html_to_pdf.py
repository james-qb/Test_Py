#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 12:23
# @Author  : qiubin
# @File    : get_html_to_pdf.py
# @Software: PyCharm
import base64
import os

import pdfkit
import requests
from bs4 import BeautifulSoup
from requests import RequestException

CURRENT_FILE_PATH = os.path.dirname(os.path.abspath('__file__'))


#  获取知乎专题文章标题及地址
def get_article_url(special_url, s_header):
    aircle_list = []
    while True:
        try:
            resp = requests.get(special_url, headers=s_header)
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
                special_url = paging['next']
                special_url = special_url.replace('zhuanlan.zhihu.com', 'zhuanlan.zhihu.com/api')
    aircle_list = aircle_list[::-1]
    print(aircle_list)
    return aircle_list


def get_image_file_as_base64_data(img_src):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    if img_src:
        print(img_src)
        resp = requests.get(img_src, headers=headers)
        resp.encoding = 'utf-8'
        image_content = resp.content
        # print(image_content)
        image_str = str(base64.b64encode(image_content), encoding='utf-8')
        print(image_str)
        return f'data:image/jpeg;base64,{image_str}'


def save_image_as_file(img_src, file_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    if img_src:
        image_content = requests.get(img_src, headers=headers).content
        with open(file_path, 'wb') as fp:
            fp.write(image_content)


def get_css_str(css_file_path):
    if css_file_path:
        with open(css_file_path, 'r', encoding='utf-8') as f2:
            css_str = "".join(f2.readlines())
            return css_str
    else:
        return ''


def save_url_html(article_url, article_title, headers):
    cur_dir = os.getcwd()
    url = article_url
    name = article_title
    # css_path = cur_dir + os.path.altsep + 'zhihu.css'
    css_path = r'D:\zhihu.css'
    savefile_name = cur_dir + os.path.altsep + name + '.html'
    while '/' in name:
        name = name.replace('/', '')
    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html, 'html.parser')
    [s.extract() for s in soup('noscript')]
    # content = soup.prettify()
    # content = soup.find(class_='Post-Main Post-NormalMain').prettify()
    content = soup.find(class_='Post-RichTextContainer').prettify()

    # print(content)
    #  content = content.replace('data-actual', '')
    #  content = content.replace('h1>', 'h2>')
    content = convert_img_tag(content, soup)

    style_css = get_css_str(css_path)
    content = """
                <!DOCTYPE html>
                <html lang="zh" data-hairline="true" data-theme="light" data-react-helmet="data-theme">
                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                    <title>{title}</title>
                    <style type="text/css">{style_css}</style>
                </head>
                <body class="WhiteBg-body" data-react-helmet="class">
                    <div id="root">
                        <div class="App">
                            <div class="LoadingBar"></div>
                            <main role="main" class="App-main">
                                <div class="Post-content">
                                    <article class="Post-Main Post-NormalMain" tabindex="-1">
                                        <header class="Post-Header">
                                            <h1 class="Post-Title">{title}</h1>
                                        </header>
                                        <div class="Post-RichTextContainer">{content}</div>
                                    </article>
                                </div>
                            </main>
                        </div>
                    </div>
                </body>
                </html>
            """.format(title=name, content=content, style_css=style_css)
    # print(content)
    with open(savefile_name, 'w', encoding='utf-8') as f:
        f.write(content)


def cover_html_to_pdf():
    curdir = os.getcwd()
    file_list = sorted(os.listdir(curdir), key=lambda x: int(x[x.find('(')+1:x.find(')')]))
    print(file_list)
    all_html_list = []
    for path in file_list:
        file_extension = os.path.splitext(path)[1]
        if file_extension == '.html':
            all_html_list.append(path)
    print(all_html_list)

    pdfkit.from_file(all_html_list, 'zhihu.pdf')


def convert_img_tag(content, soup):
    # attrs = ['data-actualsrc', 'data-original']
    attrs = ['data-original']
    image_tags = soup.select('img')
    for img_tag in image_tags:
        if not img_tag:
            continue
        if not img_tag.attrs:
            continue
        img_src = None

        old_tag = img_tag.prettify()
        for attr in attrs:
            if attr in img_tag.attrs and img_tag.attrs[attr]:
                img_src = img_tag.attrs[attr]
                break
        if img_src:
            if img_src.startswith("//"):
                img_src = "http:" + img_src
            img_tag.attrs['src'] = get_image_file_as_base64_data(img_src)
            content = content.replace(old_tag, img_tag.prettify())
    return content


# 获取网页的原始soup对象
def get_url_original_content(article_url, data=None):
    request_header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }

    req = requests.get(article_url, headers=request_header)
    req.encoding = 'utf-8'
    #  print(req.text)
    soup = BeautifulSoup(req.text, "html.parser")  # 创建BeautifulSoup对象  # 获取body部分
    return soup


if __name__ == '__main__':
    workdir = r'D:\Html2PDF'
    css_path = r'D:\zhihu.css'
    test_url = 'https://www.zhihu.com/api/v4/columns/c_1184087344080195584/items'

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

    cookie = '_zap=7d62daff-1984-4a43-b799-e4046aba28ab; d_c0="AAAZJEoUZxGPTuAspqlMiIWq7RdZnT-TtOI=|1591755307";' \
             '_ga=GA1.2.31086383.1593669470; q_c1=0258114e7f1c42c3a3700fd67833b65a|1594869340000|1591843291000; ' \
             '_xsrf=ca9c778b-bb26-479c-881a-2509e84dbd4a; '\
             'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1597028962,1597052764,' \
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

    # a_list = get_article_url(test_url, header)
    # save_data_html(a_list, header)
    # cover_html_to_pdf()
    # lsoup = get_url_original_content(r'https://zhuanlan.zhihu.com/p/111199479')
    # content = lsoup.find(class_='Post-RichTextContainer')
    # img_tags = content.find_all('img')
    # print(type(content))
    # print(type(img_tags))
    # for imag in img_tags:
    #     print(type(imag.attrs))
    #     print(imag.attrs)

    # ll = get_css_str(r'D:\zhihu.css')
    # print(ll)
    os.chdir('D:/Html2PDF')
    # save_url_html(r'https://zhuanlan.zhihu.com/p/111199479', 'JMeter点道为止系列(15)JMeter JSR223内置变量使用X', headers=header)
    # air_list = get_article_url('https://www.zhihu.com/api/v4/columns/c_1184087344080195584/items', s_header=header)
    # if air_list:
    #     for single_art in air_list:
    #         save_url_html(single_art[1], single_art[0], headers=header)

    cover_html_to_pdf()

