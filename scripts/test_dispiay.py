# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.getcwd())

from base.base_driver import inin_driver
from page.dispiay_page import Dispiay_page
from base.base_yml import yml_data_with_file
import pytest


def data_with_key(key):
    # 调用解析文件的方法yml_data_with_file，并且传递search_data的文件名
    # return拿到整个文件的字典，然后通过key去取对应的值
    return yml_data_with_file("search_data")[key]


class Test_more:

    def setup(self):
        self.driver = inin_driver()

        # 创建Dispiay_page并传入base基础参数driver、
        self.dispiay_page = Dispiay_page(self.driver)

    # 把yml_data_with_file("search_data")内的内容全部都拿到。search_data传入的文件名
    # test_search3 是 search_data里内容的字典的key
    # @pytest.mark.parametrize('content', yml_data_with_file("search_data")["test_search3"])

    # 如果test_search1里面字典的写法
    # @pytest.mark.parametrize('content', data_with_key("test_search3"))

    # 如果test_search1里面还嵌套字典的写法
    @pytest.mark.parametrize('content', data_with_key("test_search1")['name'])
    def test_search(self, content):
        # 找到显示并点击
        self.dispiay_page.click_display()
        # 找到搜索并点击
        self.dispiay_page.click_search()
        # 定位元素，并写入数据
        self.dispiay_page.input_search_text(content)
        # 点击返回
        self.dispiay_page.clik_back()
