import pytest
from itamei_api.api.login import ItaimeiLogin


class TestLogin(object):
    def setup_class(self):
        self.login = ItaimeiLogin()

    def setup(self):
        ...

    def teardown(self):
        ...

    def teardown_class(self):
        ...

    @pytest.mark.parametrize("userinfo", [{"accountName": "zhoufan", "accountPswd": "5bc8b9b17220bccbaf77e14093fd7fdc"}])
    def test_login(self, userinfo):
        self.login.doLogin(userinfo)
