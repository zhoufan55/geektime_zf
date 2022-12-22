# -*- coding: utf-8 -*-
# @Time : 2022/12/14 11:11
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : sign.py
# @Project : geektime_zf_UI
from selenium.webdriver.common.by import By
from Itaimei_ui.framework.basepage import BasePage
from Itaimei_ui.page.portal import Portal


class Sign(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)

    def open(self):
        self.driver.maximize_window()
        # 测试环境
        self.driver.get('http://trialos.test.com/login/')
        # uat环境
        # self.driver.get('https://uat.trialos.com.cn/login/')

    def signin(self, username, password):
        """
        登录
        """
        js_user = 'document.querySelector("#username").value="";'
        self.driver.execute_script(js_user)
        js = 'document.querySelector("#password").value="";'
        self.driver.execute_script(js)
        self.findElement(By.ID, 'username').send_keys(username)
        self.findElement(By.ID, 'password').send_keys(password)
        self.click(By.CSS_SELECTOR, '[type="submit"]')

    def signout(self):
        """
        退出登录
        """
        self.visi_wait(By.CSS_SELECTOR, ".itm-edc-gnav-headaction > div")
        num = len(self.findElements(By.CSS_SELECTOR, ".itm-edc-gnav-headaction > div"))
        print(num)
        self.click(By.CSS_SELECTOR, '.itm-edc-gnav-headaction > div:nth-child(%d) > div' % num)
        self.click(By.CSS_SELECTOR, "[aria-label='logout']")

    def clearInput(self):
        """
        清空登录输入框中的文字
        """
        self.visi_wait(By.ID, 'username')
        js_user = 'document.querySelector("#username").value="";'
        self.driver.execute_script(js_user)
        js = 'document.querySelector("#password").value="";'
        self.driver.execute_script(js)

    def assert_ele(self) -> str:
        """
        断言：登录成功之后，出现"我的工作台"
        """
        self.visi_wait(By.CLASS_NAME, 'workbench-company--name')
        return self.findElement(By.CLASS_NAME, 'workbench-company--name').text

    def toPortal(self, box_num) -> Portal:
        """
        点击进入portal
        """
        #
        # iframe
        self.visi_wait(By.NAME, 'workbench-iframe')
        self.driver.switch_to.frame('workbench-iframe')

        # 工作台中点击eCollect6,账号不一样可能位置不一样，传入第几个点击第几个
        box_num_ele = '#sortListBox > div:nth-child(%d)' % box_num
        self.visi_wait(By.CSS_SELECTOR, box_num_ele)
        self.click(By.CSS_SELECTOR, box_num_ele)
        portal = Portal(self.driver)
        return portal
