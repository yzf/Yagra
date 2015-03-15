#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块为工具模块，为其他模块提供各种辅助函数"""
import MySQLdb
import os
import re
import Cookie
import shelve
import sys


# 数据库相关的常量
_DB_HOST = 'localhost'
_DB_USER = 'root'
_DB_PWD = 'j'
_DB_NAME = 'yagra'
# session相关的常量
_SESSION_DIR = '/tmp/'


def add_user(username, password):
    """
    添加用户，其中password应为用户密码的md5值
    若成功，返回True，否则返回False
    """
    sql_cmd = """INSERT INTO `user`
                 (`username`, `password`) VALUES
                 ('%s', '%s');""" % (username, password)
    # 连接数据库
    db = MySQLdb.connect(_DB_HOST, _DB_USER, _DB_PWD, _DB_NAME)
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


def is_user_valid(username, password):
    """
    检测用户是否有效，验证账号和密码是否匹配
    若通过，返回True，否则返回False
    """
    sql_cmd = """SELECT 1 from `user` where
                 `username`='%s' and `password`='%s'
                 limit 1;""" % (username, password)
    # 连接数据库
    db = MySQLdb.connect(_DB_HOST, _DB_USER, _DB_PWD, _DB_NAME)
    cursor = db.cursor()
    # 进行账号密码检测
    cursor.execute(sql_cmd)
    data = cursor.fetchone()
    db.close()
    if data is None:
        return False
    return True


def has_user(username):
    """
    检测用户是否已注册
    若已注册，返回True，否则返回False
    """
    sql_cmd = """SELECT 1 from `user` where
                 `username`='%s';""" % username
    # 连接数据库
    db = MySQLdb.connect(_DB_HOST, _DB_USER, _DB_PWD, _DB_NAME)
    cursor = db.cursor()
    # 进行账号密码检测
    cursor.execute(sql_cmd)
    data = cursor.fetchone()
    db.close()
    if data is None:
        return False
    return True


def check_data_format(username, password):
    """
    检测账号username和密码password是否符合格式要求，其中：
    username：字母、数字、下划线组成，字母开头，6-16位
    password：字母和数字组成，且必须同时含有大小写字母和数字，6-12位
    若通过检测，返回True，否则返回False
    """
    regex_username = "^[a-zA-z]\w{5,15}$"
    regex_password = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{6,12}$"
    if re.match(regex_username, username) is None or\
            re.match(regex_password, password) is None:
        return False
    return True


def get_session_filename(sid):
    """
    根据sid生成session文件名
    """
    return _SESSION_DIR + 'yagra_' + sid + '.session'


def new_sid():
    """
    生成新的sid
    """
    return ''.join(map(lambda x: (hex(ord(x))[2:]), os.urandom(16)))


def new_session(username):
    """
    开始会话，进行的操作有：
    1. 把用户数据保存到服务端的session文件，session文件的命名为：sid
       session文件里面将存储的数据有：
       a. username 账号
    2. 设置客户的cookie，包括：
       a. sid 惟一标识
       其中，sid在服务端生成，
    """
    # 设置session数据
    sid = new_sid()
    session_filename = get_session_filename(sid)
    session = shelve.open(session_filename, writeback=True)
    session['username'] = username
    session.close()
    # 设置cookie数据
    cookie = Cookie.SimpleCookie()
    cookie['sid'] = sid
    print cookie


def delete_session():
    """
    结束会话，进行的操作有：
    1. 把服务端的session数据删除(删除session文件)
    2. 把cookie中的session_id的有效期设为一个很早的时间：1970年1月1日
    """
    # 删除服务端session数据(删除session文件)
    cookie_string = os.environ.get('HTTP_COOKIE', '')
    cookie = Cookie.SimpleCookie()
    cookie.load(cookie_string)
    if cookie.get('sid'):
        sid = cookie['sid'].value
        session_filename = get_session_filename(sid)
        if os.path.exists(session_filename):
            os.remove(session_filename)
    # 删除客户端cookie数据(设置sid过期)
    cookie.clear()
    cookie['sid'] = ''
    cookie['sid']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
    print cookie


def get_session():
    """
    根据cookie的sid获取session的数据
    若成功，返回数据
    若失败，返回None
    """
    cookie_string = os.environ.get('HTTP_COOKIE', '')
    cookie = Cookie.SimpleCookie()
    cookie.load(cookie_string)
    if cookie.get('sid'):
        sid = cookie['sid'].value
        session_filename = get_session_filename(sid)
        if os.path.exists(session_filename):
            session = shelve.open(session_filename, writeback=True)
            return session
    return None


def response(content_type, content):
    print content_type
    print
    print content


def redirect(url):
    with open('html/redirect.html', 'r') as redirect_file:
        content = redirect_file.read() % url
    response('Content-Type: text/html', content)
    sys.exit(0)
