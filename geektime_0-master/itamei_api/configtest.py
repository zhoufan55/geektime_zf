# -*- coding: utf-8 -*-
# @Time : 2023/1/5 15:57
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : configtest.py
# @Project : geektime_0-master
from dataclasses import asdict
from itamei_api.framework.http import Request
from itamei_api.datacls.login_datacls import LoginDataCls, UserInfoCls
from itamei_api.utils.log import log


class ItaimeiLogin(object):
    def doLogin(self, loginDa):
        loginDa1 = LoginDataCls(**loginDa)
        userInfo1 = UserInfoCls()
        request = Request()
        request.host = "https://uat.trialos.com.cn"
        request.path = "/api/sso-web/sso/sso/doLogin"
        request.method = "post"
        request.data = asdict(loginDa1)
        r = request.send()
        userInfo1.accountId = r.json()['data']['accountId']
        userInfo1.token = r.json()['data']['token']
        log.debug(r.json()['data']['accountId'])
        log.debug(r.json()['data']['token'])
        return userInfo1
