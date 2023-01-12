# -*- coding: utf-8 -*-
# @Time : 2023/1/10 12:07
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : mitmlocal.py
# @Project : geektime_0-master
import json

from mitmproxy import http, ctx


class Events:
    def request(self, flow: http.HTTPFlow) -> None:
        # flow.request.get_text()
        #
        # print(flow.request.get_text())
        if 'subjectId' in flow.request.get_text():
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
            # flow.request.get_text().replace("8ac099a984eb9be70184eb9db127027f","8ac09d3d845cb36c01845f33ad2b5829")
            # flow.request = http.Request.make(
            #     "POST",
            #     "http://trialos.test.com/api/edcr-app/query/search",
            #     flow.request.get_text().replace("8ac099a984eb9be70184eb9db127027f","8ac09d3d845cb36c01845f33ad2b5829"),
            #     {"Content-Type": "application/json"}
            # )
            # ctx.log(flow.request.get_text())


addons = [
    Events()
]
