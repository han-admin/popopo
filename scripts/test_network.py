# -*- coding: utf-8 -*-

from base.base_driver import inin_driver
from page.network_page import Network_page



class Test_more:

    def setup(self):

        self.driver = inin_driver()
        # 创建Network对象并传入driver参数

        self.network_page = Network_page(self.driver)

    # 传入 keys的参数
    def test_search_2G(self):

        # 找到搜索并点击
        self.network_page.click_seek()

        # 点击移动网络
        self.network_page.click_mesh()

        # 点击首选网络类型
        self.network_page.click_type()

        # 点击2G
        self.network_page.click_natwork_2G()
    def test_search_3G(self):

        # 找到搜索并点击
        self.network_page.click_seek()

        # 点击移动网络
        self.network_page.click_mesh()

        # 点击首选网络类型
        self.network_page.click_type()

        # 点击2G
        self.network_page.click_natwork_3G()