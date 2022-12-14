# -*- coding: utf-8 -*-
# @Time : 2022/12/14 11:11
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : sign.py
# @Project : geektime_zf_UI
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Itaimei.page.portal import Portal


class Sign(object):
    def __init__(self):
        # 浏览器复用 绕过登录或是扫码，之后若是使用浏览器，可换成cookie复用
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome("/Users/zhoufan/Desktop/zff/chromedriver", options=option)

    def open(self):
        self.driver.maximize_window()
        self.driver.get('http://trialos.test.com/login/')

    def workbench(self):
        self.driver.find_element(By.CLASS_NAME, 'workbench-item').click()

    def signin(self, username, password):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, 'username')))
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    # def signout(self):
    #     WebDriverWait(self.driver, 10).until(
    #         expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[alt="退出"]')))
    #     self.driver.find_element(By.CSS_SELECTOR, '[alt="退出"]').click()

    def assert_ele(self) -> str:
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'workbench-company--name')))
        return self.driver.find_element(By.CLASS_NAME, 'workbench-company--name').text

    def toPortal(self):
        #
        # iframe
        self.driver.switch_to.frame('workbench-iframe')
        WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#sortListBox > div:nth-child(3)')))
        self.driver.find_element(By.CSS_SELECTOR, '#sortListBox > div:nth-child(3)').click()
        portal = Portal(self.driver)
        return portal
