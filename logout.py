#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import json
import Cookie

if __name__ == '__main__':
    response_header = 'Content-Type: text/html'
    cookie = Cookie.SimpleCookie()
    cookie['username'] = ''
    cookie['username']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
    cookie['password'] = ''
    cookie['password']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
    print cookie
    print response_header
    print
    print file(r'html/login.html', 'r').read()


