#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""这个模块用来响应用户对头像的请求"""
import cgi
import os
import imghdr
import util


if __name__ == '__main__':
    IMAGE_FOLDER = 'images/'
    DEFAULT_AVATAR = 'images/00000000000000000000000000000000'
    # 获取表单数据
    form = cgi.FieldStorage()
    avatar_filename = form.getvalue('avatar', '')
    avatar_filename = cgi.escape(avatar_filename)
    # 获取指定用户的头像
    # 若文件不存在，则返回默认用户头像
    if avatar_filename:
        user_image = IMAGE_FOLDER + avatar_filename
        if os.path.exists(user_image):
            avatar = user_image
        else:
            avatar = DEFAULT_AVATAR
    # 若表单不带avatar参数，则
    #   若已登录，获取登录用户头像
    #   若未登录，则获取默认用户头像
    else:
        session = util.get_session()
        if session is not None:
            username = session.get('username', '')
            user_image = IMAGE_FOLDER + util.encode(username)
            if username and os.path.exists(user_image):
                avatar = user_image
            else:
                avatar = DEFAULT_AVATAR
            session.close()
    # 响应客户端
    content_type = 'Content-Type: image/' + imghdr.what(avatar)
    with open(avatar, 'rb') as avatar_file:
        content = avatar_file.read()
    util.response(content_type, content)
