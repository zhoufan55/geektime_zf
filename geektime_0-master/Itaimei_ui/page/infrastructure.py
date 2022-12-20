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
        eles1 = len(self.findElements(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div'))
        eles2 = len(self.findElements(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div'))
        print(eles1, eles2)

    def siteDatabaseVersion(self):
        ...

    def toPlan(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(1)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(1)')

    def toFormsets(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(2)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(2)')

    def toForms(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(3)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(3)')

    def toCodelists(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(4)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(4)')

    def toUnits(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(5)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(5)')

    def toAnalytes(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(6)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(6)')

    def toEcrfAccess(self):
        ...

    def toGuidelines(self):
        ...

    def toEditCheck(self):
        ...

    def toDerivations(self):
        ...

    def toAdvancedFunctions(self):
        ...

    def toMappingConfig(self):
        ...

    def back(self):
        hover_ele = self.findElement(By.CLASS_NAME, 'back___Ras7T')
        self.action_move(hover_ele)
        self.click(By.CLASS_NAME, 'back___Ras7T')
