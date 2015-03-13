#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块用于响应用户的注册操作"""
import cgi
import json
import util
import hashlib


def register(username, password):
    """
    进行注册操作
    若成功，返回True
    若失败，返回Flase
    """
    password = hashlib.md5(password).hexdigest()
    if util.has_user(username) == False:
        return util.add_user(username, password)
    return False


if __name__ == '__main__':
    RESPONSE_HEADER = 'Content-type: application/json'

    response_data = {'status': 1,
                     'info': '注册失败'}
    # 获取客户端的数据
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')

    if username and password and\
            util.check_data_format(username, password) is True and\
            register(username, password) is True:
        response_data['status'] = 0
        response_data['info'] = '注册成功，请进行登录'

    print RESPONSE_HEADER
    print
    # 以json格式返回操作结果给客户端
    print json.dumps(response_data)
