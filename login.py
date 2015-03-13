#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块用于处理用户的登录请求"""
import cgi
import json
import util
import hashlib


def login(username, password):
    """
    进行登录操作
    若成功，输出cookie设置给客户端，并返回True
    若失败，返回False
    """
    password = hashlib.md5(password).hexdigest()
    if util.is_user_valid(username, password):
        # 登录成功，设置cookie
        print "Set-Cookie:username=%s;" % username
        print "Set-Cookie:password=%s;" % password
        return True
    return False


if __name__ == '__main__':
    RESPONSE_HEADER = 'Content-type: application/json'

    response_data = {'status': 1,
                     'info': '账号和密码不匹配'}
    # 检查账号和密码是否匹配
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')
    # 验证通过
    if username and password and\
            util.check_data_format(username, password) is True and\
            login(username, password) == True:
        response_data['status'] = 0
        response_data['info'] = '登录成功'
    # 响应客户端
    print RESPONSE_HEADER
    print
    print json.dumps(response_data)
