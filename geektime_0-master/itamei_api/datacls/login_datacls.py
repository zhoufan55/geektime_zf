from dataclasses import dataclass


@dataclass
class LoginDataCls(object):
    accountPswd: str = None
    accountName: str = None
