#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import json
import hashlib
import MySQLdb

def login(username, password):
    sql_cmd = """SELECT 1 from `user` where
                 `username`='%s' and `password`='%s' limit 1;""" % (username, hashlib.md5(password).hexdigest())
    # 连接数据库
    db = MySQLdb.connect('localhost', 'root', 'j', 'yagra')
    cursor = db.cursor()
    # 进行账号密码检测
    cursor.execute(sql_cmd)
    data = cursor.fetchone()
    db.close()
    if data == None:
        return False
    return True

if __name__ == '__main__':
    response_header = 'Content-type: application/json'

    response_data = {'status': 1,
            'info': '账号和密码不匹配'}
    # 检查账号和密码是否匹配
    username = cgi.FieldStorage().getvalue('username', 'Unknown')
    password = cgi.FieldStorage().getvalue('password', 'Unknown')

    # 验证通过
    if login(username, password) == True:
        response_data['status'] = 0
        response_data['info'] = '登录成功'
        print "Set-Cookie:username=%s;" % username
        print "Set-Cookie:password=%s;" % hashlib.md5(password).hexdigest()
    # print response to client
    print response_header
    print #end of header
    print json.dumps(response_data)
