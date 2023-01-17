# -*- coding: utf-8 -*-
# @Time : 2023/1/17 17:10
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : SubjectDataCls.py
# @Project : geektime_0-master
from dataclasses import dataclass


@dataclass
class SubjectElements(object):
    # 1.5.1
    # new_subject: str = '.extra___2yE38 > div > div:nth-child(1) > div > div:nth-child(2)'
    # save: str = 'edc-btn-primary'
    # firstFormset: str = '.rc-virtual-list-holder > div > div > div:nth-child(2) > span > span:nth-child(2)'
    # secondForm: str = '.rc-virtual-list-holder-inner > div:nth-child(6) > span > span'
    # secondFormFitem: str = '.filed___PvH-L > div.edc-row.content___30PRa > div.edc-col.edc-col-13.col___2cbfS > div.container___SJYHX > div > label:nth-child(1) > span:nth-child(1)'
    # aess_entry_from: str = '.top___36TF0 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(2)'
    # item_single_status: str = 'div.edc-col.edc-col-9.status___3KHqg.col___2cbfS > div > div:nth-child(2) > div'
    # 1.6.1
    new_subject: str = 'div.extra___2yE38 > div > div:nth-child(6) > button'
    save: str = 'button.edc-btn.edc-btn-primary'
    firstFormset: str = '.rc-virtual-list-holder-inner > div:nth-child(2)'
    secondForm: str = '.rc-virtual-list-holder-inner > div:nth-child(6)'
    secondFormFitem: str = 'div.col___2cbfS.view___VNrLn > div > div > label:nth-child(1) > span.edc-radio'
    aess_entry_from: str = '.top___36TF0 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(2)'
    item_single_status: str = 'div.edc-col.edc-col-9.status___3KHqg.col___2cbfS > div > div:nth-child(2) > div'
