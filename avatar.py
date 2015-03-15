#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""这个模块用来响应用户对头像的请求"""
import cgi
import os
import imghdr
import util
import hashlib


if __name__ == '__main__':
    IMAGE_FOLDER = 'images/'
    DEFAULT_AVATAR = '00000000000000000000000000000000'

    form = cgi.FieldStorage()
    avatar = IMAGE_FOLDER + str(form.getvalue('avatar'))
    avatar = cgi.escape(avatar)

    session = util.get_session()

    if not os.path.exists(avatar):
        if session is not None:
            username = session.get('username')
            user_image = IMAGE_FOLDER + hashlib.md5(username).hexdigest()
            if username and os.path.exists(user_image):
                avatar = user_image
            else:
                avatar = IMAGE_FOLDER + DEFAULT_AVATAR
        else:
            avatar = IMAGE_FOLDER + DEFAULT_AVATAR

    if session is not None:
        session.close()
    # 响应客户端
    content_type = 'Content-Type: image/' + imghdr.what(avatar)
    with open(avatar, 'rb') as avatar_file:
        content = avatar_file.read()
    util.response(content_type, content)
