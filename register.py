#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块用于响应用户的注册操作"""
import os
import cgi
import json
import util


def register(username, password):
    """
    进行注册操作
    若成功，返回True
    若失败，返回Flase
    """
    if util.has_user(username) is False:
        return util.add_user(username, password)
    return False


if __name__ == '__main__':
    request_method = os.environ.get('REQUEST_METHOD', '')
    # 注册页面显示
    if request_method.upper() == 'GET':
        content_type = 'Content-Type: text/html'
        with open('html/register.html', 'r') as register_page:
            content = register_page.read()
        util.response(content_type, content)
    # 注册处理
    else:
        response_data = {'status': 1,
                         'info': '注册失败'}
        # 获取表单的数据
        form = cgi.FieldStorage()
        username = form.getvalue('username', '')
        username = cgi.escape(username)
        password = form.getvalue('password', '')
        password = cgi.escape(password)

        if username and password and\
                util.check_data_format(username, password) is True and\
                register(username, password) is True:
            response_data['status'] = 0
            response_data['info'] = '注册成功，请进行登录'
        # 响应客户端
        content_type = 'Content-Type: application/json'
        content = json.dumps(response_data)
        util.response(content_type, content)
