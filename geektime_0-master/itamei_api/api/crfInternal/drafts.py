# -*- coding: utf-8 -*-
# @Time : 2023/1/5 15:55
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : drafts.py
# @Project : geektime_0-master
import pytest

from itamei_api.datacls.draft_datacls import DraftCls


class Drafts(object):
    def draft_list(self, studyId):
        studyId1 = DraftCls(**studyId)
