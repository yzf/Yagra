#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块用于上传头像"""
import os
import cgi
import util
import imghdr
import shutil


def save_avatar(username, avatar):
    """
    保存用户的头像，只有imghdr.what能检测到的图片类型才能成功保存
    若成功，返回True
    若失败，返回False
    """
    filename = 'images/' + util.encode(username)
    filename_tmp = '/tmp/' + util.encode(username)
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
    request_method = os.environ.get('REQUEST_METHOD', '')
    # 上传页面显示
    if request_method.upper() == 'GET':
        session = util.get_session()
        if session is not None:
            content_type = 'Content-Type: text/html'
            with open('html/upload_avatar.html', 'r') as home_file:
                content = home_file.read()
            session.close()
            util.response(content_type, content)
        else:
            util.redirect('login.py')
    # 上传处理
    else:
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
            util.redirect('login.py')
        # 响应客户端
        content_type = 'Content-Type: text/html'
        with open('html/upload_result.html', 'r') as info_file:
            content = info_file.read() % info
        util.response(content_type, content)
