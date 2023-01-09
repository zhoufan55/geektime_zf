from dataclasses import dataclass


@dataclass
class LoginDataCls(object):
    accountPswd: str = None
    accountName: str = None


@dataclass
class UserInfoCls(object):
    token: str = None
    accountId: str = None
