# -*- coding: utf-8 -*-
# @Time : 2022/12/14 18:00
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : test_portal.py
# @Project : geektime_0-master
import time

from Itaimei.page.portal import Portal
from Itaimei.page.sign import Sign


class TestPortal(object):
    def setup_class(self):
        """
        初始化浏览器,登录
        """
        self.sign = Sign()
        self.sign.open()
        self.sign.signin("zhoufan55", "Zhou@1234")
        self.topor = self.sign.toPortal()

    def setup(self):
        ...

    def teardown(self):
        ...

    def teardown_class(self):
        self.sign.signout()
        self.sign.clearInput()

    def test_portal(self):
        self.topor.Infras()

        self.topor.DataColl()

        self.topor.Confi()

        self.topor.Data_Export()

        self.topor.Lab()

        self.topor.Report()

        self.topor.Coder()
        time.sleep(5)
