#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块用于上传头像"""
import os
import cgi
import util
import hashlib
import imghdr
import shutil


def save_avatar(username, avatar):
    """
    保存用户的头像，只有imghdr.what能检测到的图片类型才能成功保存
    若成功，返回True
    若失败，返回False
    """
    filename = 'images/' + hashlib.md5(username).hexdigest()
    filename_tmp = '/tmp/' + hashlib.md5(username).hexdigest()
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
    info = '头像上传失败'

    session = util.get_session()
    if session is not None:
        username = session.get('username')
        if username and\
                'avatar' in form and\
                save_avatar(username, form['avatar']):
            info = '头像上传成功'
        session.close()
    else:
        # 未登录，跳转回登录页面
        util.redirect('page_handler.py?page=html/login.html')
    # 响应客户端
    content_type = 'Content-Type: text/html'
    with open('html/upload_result.html', 'r') as info_file:
        content = info_file.read() % info
    util.response(content_type, content)
