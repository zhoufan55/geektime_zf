# -*- coding: utf-8 -*-
# @Time : 2022/12/14 15:32
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : portal.py
# @Project : geektime_0-master
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Itaimei.page.infrastructure import Infrastructure


class Portal(object):
    def __init__(self, driver):
        self.driver = driver

    def Infras(self):
        self.driver.find_element(By.CSS_SELECTOR, '[role="menu"] > li:nth-child(1)').click()
        ins = Infrastructure(self.driver)
        return ins

    def DataColl(self):
        ...

    def Confi(self):
        ...

    def Lab(self):
        ...

    def Report(self):
        ...

    def Data_Export(self):
        ...

    def Coder(self):
        ...
