#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import os
import db
import hashlib
import cgitb; cgitb.enable()

def save_avatar(username, avatar):
    filename = './images/' + hashlib.md5(username).hexdigest()
    is_success = False
    try:
        open(filename, 'wb').write(avatar.file.read())
        is_success = True
    except:
        pass
    return is_success

if __name__ == '__main__':
    form = cgi.FieldStorage()
    avatar = form['avatar']
    is_success = False
    # 保存头像
    if avatar.filename:
        # 获取登录后的用户名
        if os.environ.has_key('HTTP_COOKIE'):
            username = ''
            password = ''
            for cookie_item in os.environ['HTTP_COOKIE'].split(';'):
                cookie_item = cookie_item.strip()
                (key, value) = cookie_item.split('=')
                if key == 'username':
                    username = value
                if key == 'password':
                    password = value
            if db.is_user_valid(username, password):
                is_success = save_avatar(username, avatar)
    # 响应客户端
    print 'Content-Type: text/html'
    print
    if is_success == True:
        print '头像上传成功'
    else:
        print '头像上传失败'
