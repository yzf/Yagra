#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import json

response_header = 'Content-type: text/html'
failure_info = 'Failure'
success_info = 'Success'

if __name__ == '__main__':
    response_data = {'status': 1,
            'info': failure_info}
    # Check if username and password are correct
    check_result = True
    username = cgi.FieldStorage().getvalue('username')
    password = cgi.FieldStorage().getvalue('password')

    if check_result:
        response_data['status'] = 0
        response_data['info'] = success_info

    # print response to client
    print response_header
    print #end of header
    print json.dumps(data)
