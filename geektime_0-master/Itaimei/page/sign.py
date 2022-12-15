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

from Itaimei.framework.basepage import BasePage
from Itaimei.page.portal import Portal


class Sign(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)
        # 浏览器复用 绕过登录或是扫码，之后若是使用浏览器，可换成cookie复用

    def open(self):
        self.driver.maximize_window()
        # 测试环境
        # self.driver.get('https://uat.trialos.com.cn/login/')
        # uat环境
        self.driver.get('https://uat.trialos.com.cn/login/')

    def signin(self, username, password):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, 'username')))
        js_user = 'document.querySelector("#username").value="";'
        self.driver.execute_script(js_user)
        js = 'document.querySelector("#password").value="";'
        self.driver.execute_script(js)
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def signout(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, ".itm-edc-gnav-headaction > div:nth-child(2) > div")))
        self.driver.find_element(By.CSS_SELECTOR, ".itm-edc-gnav-headaction > div:nth-child(2) > div").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='logout']")))
        self.driver.find_element(By.CSS_SELECTOR, "[aria-label='logout']").click()

    def clearInput(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, 'username')))
        js_user = 'document.querySelector("#username").value="";'
        # self.driver.find_element(By.ID, 'username').clear()
        self.driver.execute_script(js_user)
        time.sleep(2)
        js = 'document.querySelector("#password").value="";'
        # self.driver.find_element(By.ID, 'password').clear()
        self.driver.execute_script(js)

    def assert_ele(self) -> str:
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'workbench-company--name')))
        return self.driver.find_element(By.CLASS_NAME, 'workbench-company--name').text

    def toPortal(self) -> Portal:
        #
        # iframe
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located((By.NAME, 'workbench-iframe'))
        )
        self.driver.switch_to.frame('workbench-iframe')

        # 测试环境
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#sortListBox > div:nth-child(3)')))
        # self.driver.find_element(By.CSS_SELECTOR, '#sortListBox > div:nth-child(3)').click()

        # uat环境
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#sortListBox > div:nth-child(4)')))
        self.driver.find_element(By.CSS_SELECTOR, '#sortListBox > div:nth-child(4)').click()
        portal = Portal(self.driver)
        return portal
