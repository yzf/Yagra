#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块用于处理用户的登录请求"""
import os
import cgi
import json
import util


def login(username, password):
    """
    进行登录操作
    若成功，输出cookie设置给客户端，并返回True
    若失败，返回False
    """
    if util.is_user_valid(username, password):
        # 登录成功，开启一个session
        util.new_session(username)
        return True
    return False


if __name__ == '__main__':
    request_method = os.environ.get('REQUEST_METHOD', '')
    # 登录页面显示
    if request_method.upper() == 'GET':
        content_type = 'Content-Type: text/html'
        with open('html/login.html', 'r') as login_page:
            content = login_page.read()
        util.response(content_type, content)
    # 登录处理
    else:
        response_data = {'status': 1,
                         'info': '账号和密码不匹配'}
        # 获取表单的数据
        form = cgi.FieldStorage()
        username = form.getvalue('username', '')
        username = cgi.escape(username)
        password = form.getvalue('password', '')
        password = cgi.escape(password)
        # 验证通过
        if username and password and\
                util.check_data_format(username, password) is True and\
                login(username, password) is True:
            response_data['status'] = 0
            response_data['info'] = '登录成功'
        # 响应客户端
        content_type = 'Content-Type: application/json'
        content = json.dumps(response_data)
        util.response(content_type, content)
