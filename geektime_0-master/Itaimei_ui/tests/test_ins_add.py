# -*- coding: utf-8 -*-
# @Time : 2022/12/14 17:55
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : test_ins.py
# @Project : geektime_0-master
import time
from logging import log, INFO
import pytest
from Itaimei_ui.page.sign import Sign


class TestInsAdd(object):
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
        self.toInfras.delete_draft()

    def teardown_class(self):
        # self.sign.signout()
        # self.sign.clearInput()
        ...

    # @pytest.mark.skip
    @pytest.mark.parametrize("draftName", [["draftName1"], ["draftName2"]])
    def test_ins_add_draft(self, draftName):
        self.toInfras.add_draft(draftName)
        log(INFO, draftName[0])
        assert draftName[0] in self.toInfras.assert_draft_name()

