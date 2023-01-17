# -*- coding: utf-8 -*-
# @Time : 2022/12/14 17:37
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : report.py
# @Project : geektime_0-master

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from Itaimei_ui.elementsDataCls.SubjectDataCls import SubjectElements
from Itaimei_ui.framework.basepage import BasePage
from Itaimei_ui.page.collection.subjectdetail import SubjectDetail
from Itaimei_ui.utils.log import log


class DataCollection(BasePage):
    def __init__(self, driver: WebDriver):
        # 接受外部传入的driver，用于自己内部使用
        super().__init__(driver)
        subelemnts = SubjectElements()
        # self.new_subject = '.extra___2yE38 > div > div:nth-child(1) > div > div:nth-child(2)'
        # self.save = 'edc-btn-primary'
        # self.firstFormset = '.rc-virtual-list-holder > div > div > div:nth-child(2) > span > span:nth-child(2)'
        # self.secondForm = '.rc-virtual-list-holder-inner > div:nth-child(6) > span > span'
        # self.secondFormFitem = '.filed___PvH-L > div.edc-row.content___30PRa > div.edc-col.edc-col-13.col___2cbfS > div.container___SJYHX > div > label:nth-child(1) > span:nth-child(1)'
        # self.aess_entry_from = '.top___36TF0 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(2)'
        # self.item_single_status = 'div.edc-col.edc-col-9.status___3KHqg.col___2cbfS > div > div:nth-child(2) > div'
        self.new_subject = subelemnts.new_subject
        self.save = subelemnts.save
        self.firstFormset = subelemnts.firstFormset
        self.secondForm = subelemnts.secondForm
        self.secondFormFitem = subelemnts.secondFormFitem
        self.aess_entry_from = subelemnts.aess_entry_from
        self.item_single_status = subelemnts.item_single_status

    def AddSubject(self):
        self.visi_wait(By.CSS_SELECTOR, self.new_subject)
        self.click(By.CSS_SELECTOR, self.new_subject)
        self.visi_wait(By.CLASS_NAME, self.save)
        self.click(By.CLASS_NAME, self.save)

    def add_text_assert(self, assrt_text):
        self.visi_wait(By.CSS_SELECTOR, self.firstFormset)
        text = self.findElement(By.CSS_SELECTOR, self.firstFormset).text
        assert assrt_text in text

    def ToSubjcetDetail(self):
        return SubjectDetail(self.driver)
