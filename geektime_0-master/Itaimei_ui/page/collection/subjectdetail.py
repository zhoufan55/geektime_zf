# -*- coding: utf-8 -*-
# @Time : 2023/1/13 18:47
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : subjectdetail.py
# @Project : geektime_0-master
from selenium.webdriver.common.by import By
from Itaimei_ui.page.datacollection import DataCollection
from Itaimei_ui.utils.log import log


class SubjectDetail(DataCollection):
    def __init__(self, driver):
        super().__init__(driver)

    def entry_form(self):
        self.click(By.CSS_SELECTOR, self.firstFormset)
        self.visi_wait(By.CSS_SELECTOR, self.secondForm)
        self.click(By.CSS_SELECTOR, self.secondForm)
        self.visi_wait(By.CSS_SELECTOR, self.secondFormFitem)
        self.click(By.CSS_SELECTOR, self.secondFormFitem)
        self.visi_wait(By.CLASS_NAME, self.save)
        self.click(By.CLASS_NAME, self.save)

    def entry_form_assert(self, assrt_text):
        self.visi_wait(By.CSS_SELECTOR, self.aess_entry_from)
        text = self.findElement(By.CSS_SELECTOR, self.aess_entry_from).text
        assert assrt_text in text

    def updateStatus_form(self):
        ...

    def updateStatus_item_single(self):
        self.visi_wait(By.CSS_SELECTOR, self.item_single_status)
        num = len(self.findElements(By.CSS_SELECTOR, self.item_single_status + ' > div'))
        log.debug(num)
        for i in range(1, num + 1):
            log.debug(self.item_single_status + ' > div:nth-child(%d)' % i)
            self.visi_wait(By.CSS_SELECTOR, self.item_single_status + ' > div:nth-child(%d)' % i)
            self.click(By.CSS_SELECTOR, self.item_single_status + ' > div:nth-child(%d)' % i)

    def updateStatus_item_multi(self):
        ...
