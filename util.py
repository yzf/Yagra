#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import os
import re

_DB_HOST = 'localhost'
_DB_USER = 'root'
_DB_PWD = 'j'
_DB_NAME = 'yagra'


def add_user(username, password):
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


def get_data_from_cookie():
    data = {}
    if 'HTTP_COOKIE' in os.environ:
        for cookie_item in os.environ['HTTP_COOKIE'].split(';'):
            cookie_item = cookie_item.strip()
            (key, value) = cookie_item.split('=')
            data.setdefault(key, value)
    return data


def check_data_format(username, password):
    re_username = "^[a-zA-z]\w{5,15}$"
    re_password = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{6,12}$"
    if re.match(re_username, username) is None or\
            re.match(re_password, password) is None:
        return False
    return True
