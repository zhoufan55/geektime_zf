# -*- coding: utf-8 -*-
# @Time : 2022/12/14 17:55
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : test_ins.py
# @Project : geektime_0-master
from logging import log, INFO
import pytest
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
        # self.sign.signout()
        # self.sign.clearInput()
        ...

    # @pytest.mark.skip
    @pytest.mark.parametrize("draftName", [["draftName1"], ["draftName2"]])
    def test_ins_add_draft(self, draftName):
        self.toInfras.add_draft(draftName)
        log(INFO, draftName[0])
        assert draftName[0] in self.toInfras.assert_draft_name()

    def test_delete_draft(self):
        self.toInfras.delete_draft()

    @pytest.mark.skip
    def test_ins(self):
        self.toInfras.draftManagement()
        self.toInfras.toPlan()
        self.toInfras.back()
        self.toInfras.toFormsets()
        self.toInfras.back()
        self.toInfras.toForms()
        self.toInfras.back()
        self.toInfras.toCodelists()
        self.toInfras.back()
        self.toInfras.toUnits()
        self.toInfras.back()
        self.toInfras.toAnalytes()
        self.toInfras.back()
        self.toInfras.toEcrfAccess()
        self.toInfras.back()
        self.toInfras.toGuidelines()
        self.toInfras.back()
        self.toInfras.toEditCheck()
        self.toInfras.back()
        self.toInfras.toDerivations()
        self.toInfras.back()
        self.toInfras.toAdvancedFunctions()
        self.toInfras.back()
        self.toInfras.toMappingConfig()
        self.toInfras.back()

    def test_ins_export(self):
        ...

    def test_ins_import(self):
        ...

    def test_ins_overwrite(self):
        ...

    def test_release(self):
        ...
