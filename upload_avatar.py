#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cgi
import util
import hashlib
import imghdr
import shutil


def save_avatar(username, avatar):
    filename = r'./images/' + hashlib.md5(username).hexdigest()
    filename_tmp = r'/tmp/' + hashlib.md5(username).hexdigest()
    is_success = False
    try:
        file(filename_tmp, 'wb').write(avatar.file.read())
        if imghdr.what(filename_tmp):
            shutil.copy(filename_tmp, filename)
            os.remove(filename_tmp)
            is_success = True
    except:
        pass
    return is_success


if __name__ == '__main__':
    form = cgi.FieldStorage()
    avatar = form['avatar']
    info = '头像上传失败'

    # 保存头像
    if avatar.filename:
        # 获取登录后的用户名
        cookie = util.get_data_from_cookie()
        username = cookie.get('username')
        password = cookie.get('password')
        if username and password and util.is_user_valid(username, password):
            if save_avatar(username, avatar):
                info = '头像上传成功'
        else:
            info = '请先登录'
    else:
        info = '请重新选择上传文件'

    # 响应客户端
    print 'Content-Type: text/html'
    print
    print file(r'html/info.html', 'r').read() % info
