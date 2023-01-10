# -*- coding: utf-8 -*-
# @Time : 2023/1/10 14:48
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : mitmrewrite.py
# @Project : geektime_0-master
import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    if 'id=8ac09f3684d096ba0184d0a9ee7f0461' in flow.request.pretty_url:
        res = json.loads(flow.response.content)
        res['data']['draftName'] = "mitm-modify"
        res['data']['subjectFormOid'] = "MITMOID"
        flow.response.text = json.dumps(res)
