# -*- coding: utf-8 -*-
# @Time : 2022/12/14 17:37
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : report.py
# @Project : geektime_0-master
import logging
import time

from selenium.webdriver.common.by import By
from Itaimei_ui.framework.basepage import BasePage


class Infrastructure(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def draftManagement(self):
        self.visi_wait(By.CSS_SELECTOR, '.edc-form-horizontal > div:nth-child(2)')
        self.click(By.CSS_SELECTOR, '.edc-form-horizontal > div:nth-child(2)')
        self.visi_wait(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div:nth-child(1)')
        eles1 = len(self.findElements(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(1) > div'))
        eles2 = len(self.findElements(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div'))

    def draft_num(self) -> int:
        self.visi_wait(By.CSS_SELECTOR, '.edc-form-horizontal')
        drafts = self.findElements(By.CSS_SELECTOR, '.edc-form-horizontal > div')
        draft_nums = len(drafts)
        print(draft_nums)
        return draft_nums

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
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(1)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(1)')

    def toGuidelines(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(2)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(2)')

    def toEditCheck(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(3)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(3)')

    def toDerivations(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(4)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(4)')

    def toAdvancedFunctions(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(5)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(5)')

    def toMappingConfig(self):
        hover_ele = self.findElement(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(6)')
        self.action_move(hover_ele)
        self.click(By.CSS_SELECTOR, '.menu___1g4__ > div:nth-child(2) > div:nth-child(6)')

    def add_draft(self, draftName):
        self.visi_wait(By.CLASS_NAME, 'icon-edc-add')
        self.click(By.CLASS_NAME, 'icon-edc-add')
        self.visi_wait(By.CLASS_NAME, 'headerExtra___3fjDw')
        # eles = len(self.findElements(By.CSS_SELECTOR, '.headerExtra___3fjDw > li'))
        # Create Manually
        self.click(By.CSS_SELECTOR, '.list___3zSjf > li:nth-child(2)')
        self.visi_wait(By.ID, 'draftName')
        self.findElement(By.ID, 'draftName').send_keys(draftName)
        self.click(By.CSS_SELECTOR, '.edc-row-end > div > button')
        time.sleep(0.5)

    def assert_text(self):
        text = self.findElement(
            By.CSS_SELECTOR,
            '.wrap___2wsUC > .edc-form-horizontal > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2)').text

        logging.info(text)
        return text

    def delete_draft(self):
        # ele = self.findElement(By.CSS_SELECTOR,
        #                        '.wrap___2wsUC > .edc-form-horizontal > div:nth-child(1) > div > div:nth-child(2)')
        ele = self.findElement(By.CSS_SELECTOR,
                               '.wrap___2wsUC > .edc-form-horizontal > div:nth-child(1) > div')
        self.click(By.CSS_SELECTOR,
                   '.wrap___2wsUC > .edc-form-horizontal > div:nth-child(1) > div')
        self.action_move(ele)
        nums = self.draft_num()
        print(nums)
        ele1 = self.findElement(By.CSS_SELECTOR,
                                '.wrap___2wsUC > .edc-form-horizontal > div:nth-child(1) > div > div:nth-child(2)')
        self.action_move(ele1)
        time.sleep(0.5)
        ele2 = self.findElement_dy(By.CSS_SELECTOR,
                                   'body > div:nth-child(%d) > div > div > ul > li:nth-child(2)' % nums)
        self.action_move(ele2)
        self.click(By.CSS_SELECTOR,
                   'body > div:nth-child(%d) > div > div > ul > li:nth-child(2)' % nums)
        self.findElement(By.CSS_SELECTOR, '.edc-modal-confirm-btns > button:nth-child(2)')
        self.click(By.CSS_SELECTOR, '.edc-modal-confirm-btns > button:nth-child(2)')

    def back(self):
        hover_ele = self.findElement(By.CLASS_NAME, 'back___Ras7T')
        self.action_move(hover_ele)
        self.click(By.CLASS_NAME, 'back___Ras7T')
