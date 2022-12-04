import pytest
from webUI.ceshiren import CeShiRen


class TestCeShiRenSearch(object):
    def setup_class(self):
        """
        初始化浏览器，打开页面
        """
        self.CSRen = CeShiRen()
        self.CSRen.open()
        self.search = self.CSRen.open_search()

    def setup(self):
        """
        打开搜索
        """
        self.CSRen.open_search()

    def teardown(self):
        self.search.clear_search()

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
        assert keyword in self.search.search_advanced(keyword)
