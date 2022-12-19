# -*- coding: utf-8 -*-
# @Time : 2022/12/14 15:32
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : portal.py
# @Project : geektime_0-master
import logging

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Itaimei_ui.framework.basepage import BasePage
from Itaimei_ui.page.coder import Coder
from Itaimei_ui.page.configuration import Configturation
from Itaimei_ui.page.datacollection import DataCollection
from Itaimei_ui.page.dataexport import DataExport
from Itaimei_ui.page.infrastructure import Infrastructure
from Itaimei_ui.page.lab import Lab
from Itaimei_ui.page.report import Report


class Portal(BasePage):
    def __init__(self, driver: WebDriver):
        # 接受外部传入的driver，用于自己内部使用
        super().__init__(driver)
        self.wait(By.CSS_SELECTOR, '[role="menu"] > li:nth-child(1)')
        # 获取左边菜单个数，循环取出，放入列表porElements，以供读取适用
        self.porElements = []
        num = len(self.findElements(By.CSS_SELECTOR, '[role="menu"] > li'))
        logging.info(num)
        for i in range(1, num + 1):
            ele = self.findElement(By.CSS_SELECTOR, '[role="menu"] > li:nth-child(%d)' % i)
            self.porElements.append(ele)

    def lang(self):
        """
        切换语言环境
        """
        self.click(By.CSS_SELECTOR, ".itm-edc-gnav-headaction > div:nth-child(1) > div")
        self.click(By.CSS_SELECTOR, '.edc-dropdown-menu-light > li:nth:child(2)')

    def search(self, keyword):
        """
        portal搜索功能
        """
        self.findElement(By.CLASS_NAME, 'edc-input').send_keys(keyword)
        self.click(By.CLASS_NAME, 'edc-input-search-button')

    def view(self):
        ...

    def Infras(self) -> Infrastructure:
        """
        crf构建
        """
        self.porElements[0].click()
        self.wait(By.CSS_SELECTOR, '.crf-list__container > div:nth-child(2) > div')
        self.click(By.CSS_SELECTOR,
                   '.crf-list__container > div:nth-child(2) > div:nth-child(1)')
        ins = Infrastructure(self.driver)
        return ins

    def eCRFDesignList_First(self):
        self.porElements[0].click()
        self.wait(By.CSS_SELECTOR, '.crf-list__container > div:nth-child(2) > div')
        # 获取第一页项目数量
        projectEles = []
        pros = len(self.findElements(By.CSS_SELECTOR, '.crf-list__container > div:nth-child(2) > div'))
        logging.info(pros)
        if pros > 0:
            # 循环获取第一页所有项目列表元素
            for i in range(1, pros + 1):
                ele = self.findElement(By.CSS_SELECTOR,
                                       '.crf-list__container > div:nth-child(2) > div:nth-child(%d)' % i)
                projectEles.append(ele)
            self.click(By.CSS_SELECTOR,
                       '.crf-list__container > div:nth-child(2) > div:nth-child(1)')
        else:
            pass

    def DataColl(self) -> DataCollection:
        """
        数据采集driver
        """
        self.porElements[1].click()
        dac = DataCollection(self.driver)
        return dac

    def EcollectList_First(self):
        ...

    def Confi(self) -> Configturation:
        """
        配置configuration   driver
        """
        self.porElements[3].click()
        conf = Configturation(self.driver)
        return conf

    def SettingsList_First(self):
        ...

    def Lab(self) -> Lab:
        """
        实验室driver
        """
        self.porElements[4].click()
        lab = Lab(self.driver)
        return lab

    def LabList_First(self):
        ...

    def Report(self) -> Report:
        """
        报表driver
        """
        self.porElements[5].click()
        report = Report(self.driver)
        return report

    def ReportList_First(self):
        ...

    def Data_Export(self) -> DataExport:
        """
        数据导出driver
        """
        self.porElements[6].click()
        daex = DataExport(self.driver)
        return daex

    def ExportList_First(self):
        ...

    def Coder(self) -> Coder:
        """
        编码driver
        """
        self.porElements[7].click()
        coder = Coder(self.driver)
        return coder

    def CoderList_First(self):
        """
        编码列表
        """
        ...
