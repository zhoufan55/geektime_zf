# -*- coding: utf-8 -*-
# @Time : 2022/12/14 11:11
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : test_login.py
# @Project : geektime_zf_UI
import pytest

from Itaimei.page.sign import Sign


class TestLogin(object):
    def setup_class(self):
        """
        初始化浏览器
        """
        self.sign = Sign()
        self.sign.open()
        self.sign.clearInput()

    def setup(self):
        self.sign.clearInput()

    def teardown(self):
        ...

    def teardown_class(self):
        self.sign.toPortal(1)
        self.sign.signout()

    @pytest.mark.parametrize('username,password', [('zhoufan', 'Zhou@123456')])
    def test_signin(self, username, password):
        self.sign.signin(username, password)
        assert "我的工作台" in self.sign.assert_ele()
