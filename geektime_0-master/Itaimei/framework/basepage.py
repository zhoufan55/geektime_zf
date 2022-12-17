# -*- coding: utf-8 -*-
# @Time : 2022/12/15 16:41
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : basepage.py
# @Project : geektime_0-master
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver: WebDriver = None):
        if driver is not None:
            self.driver = driver
        else:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome("/Users/a404/chromedriver", options=option)

    def wait(self, by, element, seconds=10):
        return WebDriverWait(self.driver, seconds).until(
            expected_conditions.visibility_of_all_elements_located((by, element))
        )

    def findElement(self, by, element, seconds=10):
        self.wait(by, element, seconds)
        return self.driver.find_element(by, element)

    def findElements(self, by, element, seconds=10):
        self.wait(by, element, seconds)
        return self.driver.find_elements(by, element)

    def click(self, by, element):
        return self.findElement(by, element).click()

    def base_page(self):
        ...
