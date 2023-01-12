# -*- coding: utf-8 -*-
# @Time : 2023/1/10 14:48
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : mitmrewrite.py
# @Project : geektime_0-master
import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    if 'query/search' in flow.request.pretty_url:
        res = json.loads(flow.response.content)
        res['data']['rows'][0]['formName'] = "mitm-modify"
        # res['data']['subjectFormOid'] = "MITMOID"
        flow.response.text = json.dumps(res)
