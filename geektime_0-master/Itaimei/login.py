# -*- coding: utf-8 -*-
# @Time : 2022/12/14 11:11
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : login.py
# @Project : geektime_zf_UI
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self):
        self.driver.maximize_window()
        self.driver.get('http://trialos.test.com/')

    def login(self, username, password):
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
