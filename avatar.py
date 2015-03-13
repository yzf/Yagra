#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""这个模块用来响应用户对头像的请求"""
import cgi
import os
import imghdr
import util
import hashlib


if __name__ == '__main__':
    IMAGE_FOLDER = r'./images/'
    DEFAULT_AVATAR = '00000000000000000000000000000000'

    form = cgi.FieldStorage()
    avatar = IMAGE_FOLDER + str(form.getvalue('avatar'))

    if os.path.exists(avatar) is False:
        cookie = util.get_data_from_cookie()
        username = cookie.get('username')
        user_image = IMAGE_FOLDER + hashlib.md5(username).hexdigest()
        if username and os.path.exists(user_image):
            avatar = user_image
        else:
            avatar = IMAGE_FOLDER + DEFAULT_AVATAR

    print 'Content-Type: image/' + imghdr.what(avatar)
    print
    print file(avatar, 'rb').read()
