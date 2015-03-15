#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该模块用于处理用户的退出登录请求"""
import util


if __name__ == '__main__':
    # 结束回话
    util.delete_session()
    # 响应客户端
    util.redirect('page_handler.py?page=login.html')
