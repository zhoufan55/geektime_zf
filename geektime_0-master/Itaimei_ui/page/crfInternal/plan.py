# -*- coding: utf-8 -*-
# @Time : 2022/12/20 10:57
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : plan.py
# @Project : geektime_0-master
from selenium.webdriver.common.by import By

from Itaimei_ui.page.infrastructure import Infrastructure


class Plans(Infrastructure):
    def __init__(self, driver):
        super().__init__(driver)

    def add_plan(self):
        self.click(By.CLASS_NAME, 'edc-btn edc-btn-primary')

    def delete_plan(self):
        ...
