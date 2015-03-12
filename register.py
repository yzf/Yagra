#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import json
import util
import hashlib

def register(username, password):
    password = hashlib.md5(password).hexdigest()
    if util.has_user(username) == False:
        return util.add_user(username, password)
    return False

if __name__ == '__main__':
    response_header = 'Content-type: application/json'

    response_data = {'status': 1,
            'info': '注册失败'}
    # 获取客户端的数据
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')

    if username and password:
        if register(username, password) == True:
            response_data['status'] = 0
            response_data['info'] = '注册成功'

    print response_header
    print #end of header
    # 以json格式返回操作结果给客户端
    print json.dumps(response_data)
