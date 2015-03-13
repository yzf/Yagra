#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块为工具模块，为其他模块提供各种辅助函数"""
import MySQLdb
import os
import re

_DB_HOST = 'localhost'
_DB_USER = 'root'
_DB_PWD = 'j'
_DB_NAME = 'yagra'


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


def get_data_from_cookie():
    """
    从cookie中提取数据，返回dict格式的数据
    """
    data = {}
    if 'HTTP_COOKIE' in os.environ:
        for cookie_item in os.environ['HTTP_COOKIE'].split(';'):
            cookie_item = cookie_item.strip()
            (key, value) = cookie_item.split('=')
            data.setdefault(key, value)
    return data


def check_data_format(username, password):
    """
    检测账号username和密码password是否符合格式要求，其中：
    username：字母、数字、下划线组成，字母开头，6-16位
    password：字母和数字组成，且必须同时含有大小写字母和数字，6-12位
    若通过检测，返回True，否则返回False
    """
    re_username = "^[a-zA-z]\w{5,15}$"
    re_password = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{6,12}$"
    if re.match(re_username, username) is None or\
            re.match(re_password, password) is None:
        return False
    return True
