# -*- coding: utf-8 -*-
# @Time : 2022/12/15 16:41
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : basepage.py
# @Project : geektime_0-master
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage(object):
    def __init__(self, driver: WebDriver = None):
        if driver is not None:
            self.driver = driver
        else:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome("/Users/zhoufan/Desktop/zff/chromedriver", options=option)

    def base_page(self):
        ...
