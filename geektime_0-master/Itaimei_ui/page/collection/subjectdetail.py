# -*- coding: utf-8 -*-
# @Time : 2023/1/13 18:47
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : subjectdetail.py
# @Project : geektime_0-master
from selenium.webdriver.common.by import By

from Itaimei_ui.elementsDataCls.SubjectDataCls import SubjectElements
from Itaimei_ui.framework.basepage import BasePage
from Itaimei_ui.utils.log import log


class SubjectDetail(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        subelemnts = SubjectElements()
        self.firstFormset = subelemnts.firstFormset
        self.secondForm = subelemnts.secondForm
        self.secondFormFitem = subelemnts.secondFormFitem
        self.save = subelemnts.save
        self.aess_entry_from = subelemnts.aess_entry_from
        self.item_single_status = subelemnts.item_single_status
        self.item_mutil_status = subelemnts.item_mutil_status
        self.init_multi_records = subelemnts.init_multi_records
        self.add_multi = subelemnts.multi_add

    def entry_form(self):
        self.click(By.CSS_SELECTOR, self.firstFormset)
        self.visi_wait(By.CSS_SELECTOR, self.secondForm)
        self.click(By.CSS_SELECTOR, self.secondForm)
        self.visi_wait(By.CSS_SELECTOR, self.secondFormFitem)
        self.click(By.CSS_SELECTOR, self.secondFormFitem)
        self.visi_wait(By.CSS_SELECTOR, self.save)
        self.click(By.CSS_SELECTOR, self.save)

    def entry_form_assert(self, assrt_text):
        self.visi_wait(By.CSS_SELECTOR, self.aess_entry_from)
        text = self.findElement(By.CSS_SELECTOR, self.aess_entry_from).text
        assert assrt_text in text

    def updateStatus_form(self):
        ...

    def updateStatus_item_single(self):
        self.visi_wait(By.CSS_SELECTOR, self.item_single_status)
        num = len(self.findElements(By.CSS_SELECTOR, self.item_single_status + ' > div.edc-space-item'))
        log.debug(num)
        for i in range(1, num + 1):
            log.debug(self.item_single_status + ' > div:nth-child(%d)' % i)
            self.visi_wait(By.CSS_SELECTOR, self.item_single_status + ' > div:nth-child(%d)' % i)
            self.click(By.CSS_SELECTOR, self.item_single_status + ' > div:nth-child(%d)' % i)

    def updateStatus_item_multi(self):
        self.visi_wait(By.CSS_SELECTOR, self.item_mutil_status)
        num = len(self.findElements(By.CSS_SELECTOR, self.item_mutil_status + ' > div.edc-space-item'))
        log.debug(num)
        for i in range(1, num + 1):
            log.debug(self.item_mutil_status + ' > div:nth-child(%d)' % i)
            self.visi_wait(By.CSS_SELECTOR, self.item_mutil_status + ' > div:nth-child(%d)' % i)
            self.click(By.CSS_SELECTOR, self.item_mutil_status + ' > div:nth-child(%d)' % i)

    def add_multi_record(self):
        self.visi_wait(By.CSS_SELECTOR, self.add_multi)
        num_init = len(self.findElements(By.CSS_SELECTOR, self.init_multi_records + ' > tr'))
        log.debug(num_init)
        self.click(By.CSS_SELECTOR, self.add_multi)
        num_after = len(self.findElements(By.CSS_SELECTOR, self.init_multi_records + ' > tr'))
        log.debug(num_after)
