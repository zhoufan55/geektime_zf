# -*- coding: utf-8 -*-
# @Time : 2023/1/10 12:07
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : mitmlocal.py
# @Project : geektime_0-master

from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if 'id=8ac09f3684d096ba0184d0a9ee7f0461' in flow.request.pretty_url:
        # flow.response = http.Response.make(
        #     200,
        #     b'hello world',
        #     {"Content-Type": "application/json"}
        # )
        with open('hh.json') as f:
            flow.response = http.Response.make(
                200,
                f.read(),
                {"Content-Type": "application/json"}
            )



