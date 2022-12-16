# -*- coding: utf-8 -*-
# @Time : 2022/12/14 15:32
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : portal.py
# @Project : geektime_0-master
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Itaimei.framework.basepage import BasePage
from Itaimei.page.coder import Coder
from Itaimei.page.configuration import Configturation
from Itaimei.page.datacollection import DataCollection
from Itaimei.page.dataexport import DataExport
from Itaimei.page.infrastructure import Infrastructure
from Itaimei.page.lab import Lab
from Itaimei.page.report import Report


class Portal(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[role="menu"] > li:nth-child(1)')))
        self.ins_ele = self.driver.find_element(By.CSS_SELECTOR, '[role="menu"] > li:nth-child(1)')
        self.ecoll = self.driver.find_element(By.CSS_SELECTOR, '[role="menu"] > li:nth-child(2)')
        self.settings = self.driver.find_element(By.CSS_SELECTOR, '[role="menu"] > li:nth-child(3)')
        self.lab = self.driver.find_element(By.CSS_SELECTOR, '[role="menu"] > li:nth-child(4)')
        self.report = self.driver.find_element(By.CSS_SELECTOR, '[role="menu"] > li:nth-child(5)')
        self.export = self.driver.find_element(By.CSS_SELECTOR, '[role="menu"] > li:nth-child(6)')
        self.coder = self.driver.find_element(By.CSS_SELECTOR, '[role="menu"] > li:nth-child(7)')

    def lang(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, ".itm-edc-gnav-headaction > div:nth-child(1) > div")))
        self.driver.find_element(By.CSS_SELECTOR, ".itm-edc-gnav-headaction > div:nth-child(1) > div").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, '.edc-dropdown-menu-light > li:nth:child(2)')))
        self.driver.find_element(By.CSS_SELECTOR, '.edc-dropdown-menu-light > li:nth:child(2)').click()

    def search(self, keyword):
        self.driver.find_element(By.CLASS_NAME, 'edc-input').send_keys(keyword)
        self.driver.find_element(By.CLASS_NAME, 'edc-input-search-button').click()

    def view(self):
        ...

    def Infras(self):
        self.ins_ele.click()
        ins = Infrastructure(self.driver)
        return ins

    def eCRFDesignList_First(self):
        ...

    def DataColl(self):
        self.ecoll.click()
        dac = DataCollection(self.driver)
        return dac

    def EcollectList_First(self):
        ...

    def Confi(self):
        self.settings.click()
        conf = Configturation(self.driver)
        return conf

    def SettingsList_First(self):
        ...

    def Lab(self):
        self.lab.click()
        lab = Lab(self.driver)
        return lab

    def LabList_First(self):
        ...

    def Report(self):
        self.report.click()
        report = Report(self.driver)
        return report

    def ReportList_First(self):
        ...

    def Data_Export(self):
        self.export.click()
        daex = DataExport(self.driver)
        return daex

    def ExportList_First(self):
        ...

    def Coder(self):
        self.coder.click()
        coder = Coder(self.driver)
        return coder

    def CoderList_First(self):
        ...
