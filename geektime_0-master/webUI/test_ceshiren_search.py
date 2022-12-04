import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCeshirenSearch():
    def setup_class(self):
        """
        初始化浏览器，打开页面
        """
        self.driver = webdriver.Chrome('/Users/a404/Workspace/ChromeDriverMac/chromedriver')
        self.driver.maximize_window()
        self.driver.get('https://ceshiren.com/')

    def setup(self):
        """
        打开搜索
        """
        self.driver.find_element(By.ID, 'search-button').click()
        # self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.find_element(By.ID, 'search-button').click()
        self.driver.find_element(By.CSS_SELECTOR, '[title="清除搜索内容"]').click()

    def teardown_class(self):
        ...

    @pytest.mark.parametrize("keyword", [
        'selenium',
        'appium',
        'pytest'
    ])
    def test_search(self, keyword):
        """
        Test that ceshiren search works as expected.
        """
        self.driver.find_element(By.ID, 'search-term').send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '[title="打开高级搜索"]').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'topic-title')))
        assert keyword in self.driver.find_element(By.CLASS_NAME, 'topic-title').text.lower()
