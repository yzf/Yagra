#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import json
import hashlib
import MySQLdb

def register(username, password):
    sql_cmd = """INSERT INTO `user`
                 (`username`, `password`) VALUES
                 ('%s', '%s');""" % (username, hashlib.md5(password).hexdigest())
    # 连接数据库
    db = MySQLdb.connect('localhost', 'root', 'j', 'yagra')
    # 获取操作游标
    cursor = db.cursor()
    # 进行插入操作
    is_success = True
    try:
        cursor.execute(sql_cmd)
        db.commit()
    except:
        is_success = False
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()
    return is_success

if __name__ == '__main__':
    response_header = 'Content-type: application/json'

    response_data = {'status': 1,
            'info': '注册失败'}
    # 获取客户端的数据
    username = cgi.FieldStorage().getvalue('username', 'Unknown')
    password = cgi.FieldStorage().getvalue('password', 'Unknown')

    if username != 'Unknown' and password != 'Unknown':
        if register(username, password) == True:
            response_data['status'] = 0
            response_data['info'] = '注册成功'

    print response_header
    print #end of header
    # 以json格式返回操作结果给客户端
    print json.dumps(response_data)
