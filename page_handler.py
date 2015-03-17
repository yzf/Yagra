#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块用于静态页面的获取，包括html、css和js"""
import cgi
import os
import util


if __name__ == '__main__':
    PAGE_MAP = {
        'common.css': 'css/common.css',
        'common.js': 'js/common.js',
        'login.js': 'js/login.js',
        'register.js': 'js/register.js'
    }
    # 获取表单参数
    page = cgi.FieldStorage().getvalue('page', '')
    page = cgi.escape(page)
    # 防止目录遍历攻击
    page = os.path.basename(page)

    flag = False
    if page and page in PAGE_MAP:
        filename = PAGE_MAP[page]
        # 文件存在，且只能是html、css和js文件
        if os.path.exists(filename) and\
           ('.html' in filename or '.css' in filename or '.js' in filename):
            if '.html' in filename:
                file_type = 'html'
            elif '.css' in filename:
                file_type = 'css'
            else:
                file_type = 'javascript'
            flag = True
            # 响应客户端
            content_type = 'Content-type: text/' + file_type
            with open(filename, 'r') as page_file:
                content = page_file.read()
    # 出错
    if flag is False:
        content_type = 'Content-type: text/html'
        content = 'No such page'
        with open('html/info.html', 'r') as info_file:
            content = info_file.read() % '页面不存在'
    # 响应客户端
    util.response(content_type, content)
