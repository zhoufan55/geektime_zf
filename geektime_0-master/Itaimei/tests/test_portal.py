# -*- coding: utf-8 -*-
# @Time : 2022/12/14 18:00
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : test_portal.py
# @Project : geektime_0-master

from Itaimei.page.portal import Portal
from Itaimei.page.sign import Sign


class TestPortal(object):
    def setup_class(self):
        """
        初始化浏览器
        """
        self.por = Sign().toPortal()

    def setup(self):
        ...
        # self.sign.workbench()

    def teardown(self):
        ...

    def teardown_class(self):
        ...

    def test_portal(self, username, password):
        ...
