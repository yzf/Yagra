#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
import util


if __name__ == '__main__':
    session = util.get_session()
    if session is not None:
        content_type = 'Content-Type: text/html'
        with open('html/home.html', 'r') as home_file:
            content = home_file.read()
        session.close()
        util.response(content_type, content)
    else:
        util.redirect('page_handler.py?page=login.html')
