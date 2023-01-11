# -*- coding: utf-8 -*-
# @Time : 2022/12/14 18:00
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : test_datacoll.py
# @Project : geektime_0-master
from Itaimei_ui.page.sign import Sign


class TestCollect(object):
    def setup_class(self):
        """
        初始化浏览器,登录
        """
        self.sign = Sign()
        self.sign.open()
        self.sign.clearInput()
        self.sign.signin("zhoufan55", "Zhou@1234")
        self.toDataColl = self.sign.toPortal(4).DataColl("coder项目001")

    def setup(self):
        ...

    def teardown(self):
        ...

    def teardown_class(self):
        ...

    def test_addsubject(self):
        self.toDataColl.AddSubject()
        self.toDataColl.add_text_assert('筛选期/D-14~D-1#1')

    def test_entryform(self):
        self.toDataColl.entry_form()
        self.toDataColl.entry_form_assert("编辑")

    def test_updateStatus(self):
        self.toDataColl.updateStatus_item_single()
