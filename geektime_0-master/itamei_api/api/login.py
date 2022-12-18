from dataclasses import asdict
import requests
from itamei_api.datacls.login_datacls import LoginDataCls


class ItaimeiLogin(object):
    def doLogin(self, loginDa):
        loginDa1 = LoginDataCls(**loginDa)
        url = "https://uat.trialos.com.cn/api/sso-web/sso/sso/doLogin"
        data = asdict(loginDa1)
        r = requests.post(url=url, json=data)
        return r.json()
