#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import os

if __name__ == '__main__':
    # 获取参数
    page = cgi.FieldStorage().getvalue('page')

    flag = False
    if page:
        file_name = page.strip()
        # 检测页面文件是否存在，且只能是html、css和js文件
        if os.path.exists(file_name) and ('.html' in file_name or
                                          '.css' in file_name or
                                          '.js' in file_name):
            file_type = ''
            if '.html' in file_name:
                file_type = 'html'
            elif '.css' in file_name:
                file_type = 'css'
            else:
                file_type = 'javascript'
            flag = True
            # 响应客户端
            print 'Content-type: text/' + file_type
            print
            print file(file_name, 'r').read()

    # 出错
    if flag is False:
        print 'Content-type: text/html'
        print
        print 'No such page'
