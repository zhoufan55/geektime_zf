# -*- coding: utf-8 -*-
# @Time : 2022/12/14 17:37
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : report.py
# @Project : geektime_0-master

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Itaimei_ui.framework.basepage import BasePage
from Itaimei_ui.utils.log import log


class DataCollection(BasePage):
    def __init__(self, driver: WebDriver):
        # 接受外部传入的driver，用于自己内部使用
        super().__init__(driver)
        self.new_subject = '.extra___2yE38 > div > div:nth-child(1) > div > div:nth-child(2)'
        self.save = 'edc-btn-primary'
        self.firstFormset = '.rc-virtual-list-holder > div > div > div:nth-child(2) > span > span:nth-child(2)'

    def AddSubject(self):
        self.visi_wait(By.CSS_SELECTOR, self.new_subject)
        self.click(By.CSS_SELECTOR, self.new_subject)
        self.visi_wait(By.CLASS_NAME, self.save)
        self.click(By.CLASS_NAME, self.save)

    def add_text_assert(self, assrt_text):
        self.visi_wait(By.CSS_SELECTOR, self.firstFormset)
        text = self.findElement(By.CSS_SELECTOR, self.firstFormset).text
        assert assrt_text in text


