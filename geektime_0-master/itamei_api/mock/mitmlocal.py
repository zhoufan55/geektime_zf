# -*- coding: utf-8 -*-
# @Time : 2023/1/10 12:07
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : mitmlocal.py
# @Project : geektime_0-master

from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if 'id=2c9c812f82aec1300182b3c334f97fa7' in flow.request.pretty_url:
        # flow.response = http.Response.make(
        #     200,
        #     b'hello world',
        #     {"Content-Type": "application/json"}
        # )
        # with open('hh.json') as f:
        #     flow.response = http.Response.make(
        #         200,
        #         f.read(),
        #         {"Content-Type": "application/json"}
        #     )
        flow.request.query['id'] = '8a8dbb5e857753ef0185948d8d54600e'



