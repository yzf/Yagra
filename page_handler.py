#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import os

response_header = 'Content-type: text/html'
html_dir = 'html/'

if __name__ == '__main__':
    page = cgi.FieldStorage().getvalue('p')
    print response_header
    print #end of header
    if page == None:
        print 'Query string error!'
    else:
        file_name = html_dir + page + r'.html'
        if os.path.exists(file_name):
            print file(file_name, 'r').read()
        else:
            print 'No such page'
