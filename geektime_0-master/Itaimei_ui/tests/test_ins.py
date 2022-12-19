# -*- coding: utf-8 -*-
# @Time : 2022/12/14 17:55
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : test_ins.py
# @Project : geektime_0-master
from Itaimei_ui.page.sign import Sign


class TestIns(object):
    def setup_class(self):
        """
        初始化浏览器
        """
        self.sign = Sign()
        self.sign.open()
        self.sign.signin("zhoufan5555", "Zhou@123")
        self.toInfras = self.sign.toPortal(1).Infras()

    def setup(self):
        ...

    def teardown(self):
        ...

    def teardown_class(self):
        self.sign.signout()
        self.sign.clearInput()

    def test_ins(self):
        self.toInfras.draftManagement()
        self.toInfras.back()
