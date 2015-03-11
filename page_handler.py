#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import os

if __name__ == '__main__':
    # get the page variable
    page = cgi.FieldStorage().getvalue('page')
    flag = False
    if page != None:
        file_name = page.strip()
        # check if the page's file exists
        if os.path.exists(file_name) and file_name.find('.py') == -1:
            file_type = 'html'
            if file_name.find('.css') != -1:
                file_type = 'css'
            elif file_name.find('.js') != -1:
                file_type = 'javascript'
            flag = True
            print 'Content-type: text/' + file_type
            print #end of header
            print file(file_name, 'r').read()
    # Error
    if flag == False:
        print 'Content-type: text/html'
        print #end of header
        print 'No such page'
