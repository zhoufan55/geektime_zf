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

    @pytest.mark.parametrize("userinfo", [{"accountName": "zhoufan55", "accountPswd": "7733be56668f916d617b8a4950931e46"}])
    def test_login(self, userinfo):
        self.login.doLogin(userinfo)
