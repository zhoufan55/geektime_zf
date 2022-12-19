# -*- coding: utf-8 -*-
# @Time : 2022/12/14 17:37
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : report.py
# @Project : geektime_0-master
from selenium.webdriver.common.by import By

from Itaimei_ui.framework.basepage import BasePage


class Infrastructure(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def draftManagement(self):
        self.wait(By.CSS_SELECTOR, '.wrap___2wsUC > .edc-form-horizontal > div:nth-child(2)')
        self.click(By.CSS_SELECTOR, '.wrap___2wsUC > .edc-form-horizontal > div:nth-child(2)')
        self.wait(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(1)')
        eles = len(self.findElements(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div'))
        print(eles)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(1)')

    def siteDatabaseVersion(self):
        ...

    def back(self):
        self.click(By.CLASS_NAME, 'back___Ras7T')
