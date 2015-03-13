#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块用于处理用户的退出登录请求"""
import cgi
import json
import Cookie


if __name__ == '__main__':
    RESPONSE_HEADER = 'Content-Type: text/html'
    # 把cookie中的username和password的有效期设置为已经过去的时间
    cookie = Cookie.SimpleCookie()
    cookie['username'] = ''
    cookie['username']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
    cookie['password'] = ''
    cookie['password']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'

    print cookie
    print RESPONSE_HEADER
    print
    print file(r'html/login.html', 'r').read()
