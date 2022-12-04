from selenium import webdriver
from selenium.webdriver.common.by import By
from webUI.search import Search


class CeShiRen(object):
    def __init__(self):
        self.driver = None

    def open(self):
        self.driver = webdriver.Chrome('/Users/a404/Workspace/ChromeDriverMac/chromedriver')
        self.driver.maximize_window()
        self.driver.get('https://ceshiren.com/')

    def open_search(self):
        self.driver.find_element(By.ID, 'search-button').click()
        search = Search(self.driver)
        return search


