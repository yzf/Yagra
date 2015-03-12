#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import os
import imghdr

if __name__ == '__main__':
    default_avatar = r'./images/00000000000000000000000000000000'
    form = cgi.FieldStorage()
    avatar = r'./images/' + form.getvalue('avatar')

    if os.path.exists(avatar) == False:
        avatar = default_avatar

    print 'Content-Type: image/' + imghdr.what(avatar)
    print
    print file(avatar, 'rb').read()
