# -*- coding: utf-8 -*-
# @Time : 2023/1/5 15:58
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : draft_datacls.py
# @Project : geektime_0-master
from dataclasses import dataclass


@dataclass
class DraftCls(object):
    studyId: str = None
