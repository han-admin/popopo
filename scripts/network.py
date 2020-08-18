# -*- coding: utf-8 -*-

# import os, sys
# sys.path.append(os.getcwd())


from base.base_driver import inin_driver

import pytest


class Test_more:

    def setup(self):
        self.driver = inin_driver()


    # 根据keys的值来执行多次 def函数
    @pytest.mark.parametrize('keys', ["//*[contains(@text,'2G')]", "//*[contains(@text,'3G')]"])
    # 传入 keys的参数
    def test_search(self, keys):

        # 找到搜索并点击
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()

        # 点击移动网络
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()

        # 点击首选网络类型
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()

        # 点击2G
        self.driver.find_element_by_xpath(keys).click()
