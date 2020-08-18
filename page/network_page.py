# -*- coding: utf-8 -*-

import pytest
from selenium.webdriver.common.by import By


class Network_page:



    # 使用init来接收driver
    def __init__(self, driver):
        self.driver = driver

    # 创建搜索函数
    def click_seek(self):
        # 找到搜索并点击
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()

    # 创建移动网络函数
    def click_mesh(self):
        # 点击移动网络
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(@text,'移动网络')]").click()

    # 创建首选网络类型函数
    def click_type(self):
        # 点击首选网络类型
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()

    # 创建选择2G或者3G函数
    def click_natwork_2G(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    # 创建选择2G或者3G函数
    def click_natwork_3G(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
