#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import os
import imghdr
import util
import hashlib
import cgitb; cgitb.enable()

if __name__ == '__main__':
    image_folder = r'./images/'
    default_avatar = '00000000000000000000000000000000'
    form = cgi.FieldStorage()
    avatar = image_folder + str(form.getvalue('avatar'))

    if os.path.exists(avatar) == False:
        cookie = util.get_data_from_cookie()
        username = cookie.get('username')
        user_image = image_folder + hashlib.md5(username).hexdigest()
        if username and os.path.exists(user_image):
            avatar = user_image
        else:
            avatar = image_folder + default_avatar

    print 'Content-Type: image/' + imghdr.what(avatar)
    print
    print file(avatar, 'rb').read()
