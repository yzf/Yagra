#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import json
import db
import hashlib

def login(username, password):
    password = hashlib.md5(password).hexdigest()
    if db.is_user_valid(username, password):
        # 登录成功，设置cookie
        print "Set-Cookie:username=%s;" % username
        print "Set-Cookie:password=%s;" % password
        return True
    return False

if __name__ == '__main__':
    response_header = 'Content-type: application/json'

    response_data = {'status': 1,
            'info': '账号和密码不匹配'}
    # 检查账号和密码是否匹配
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')
    # 验证通过
    if login(username, password) == True:
        response_data['status'] = 0
        response_data['info'] = '登录成功'
    # print response to client
    print response_header
    print #end of header
    print json.dumps(response_data)
