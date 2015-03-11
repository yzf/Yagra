#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import json

def login(username, password):
    sql_cmd = """SELECT 1 from `user` where
                 `username`='%s' and `password`=password('%s');""" % (username, password)
    return sql_cmd

if __name__ == '__main__':
    response_header = 'Content-type: application/json'

    response_data = {'status': 1,
            'info': '账号和密码不匹配'}
    # 检查账号和密码是否匹配
    username = cgi.FieldStorage().getvalue('username', 'Unknown')
    password = cgi.FieldStorage().getvalue('password', 'Unknown')

    # print response to client
    print response_header
    print #end of header
    response_data['info'] = login(username, password)
    print json.dumps(response_data)
