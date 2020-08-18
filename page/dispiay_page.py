# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_action import BaceAction

class Dispiay_page(BaceAction):
    # 点击显示
    display_button = By.XPATH, "//*[contains(@text,'显示')]"

    # 点击搜索
    search_button = By.ID, "com.android.settings:id/search"

    # 搜索框
    input_text_view = By.ID, "android:id/search_src_text"

    # 返回按钮
    back_button =By.CLASS_NAME, "android.widget.ImageButton"


    def __init__(self, driver):
        BaceAction.__init__(self, driver)
        self.click_display()

    def click_display(self):
        """        # 调用自己的find_element 来点击显示
        self.find_element(self.display_button).click()"""
        self.click(self.display_button)

    # 点击搜索函数
    def click_search(self):
        """        # 调用自己的find_element 来点击搜索
        self.find_element(self.search_button).click()"""


        self.click(self.search_button)

    # 输入数据函数,传入text参数
    def input_search_text(self, text):
        """# 调用系统的,find_element 定位元素，并写入数据
        # self.driver.find_element(By.ID, "android:id/search_src_text").send_keys("你好")

        # 调用自己的find_element 来写入数据
        self.find_element(self.input_text_view).send_keys(text)"""

        self.input_text(self.input_text_view, text)

    # 点击返回函数
    def clik_back(self):
        """# 调用自己的find_element 来点击返回
        self.find_element(self.back_button).click()"""

        self.click(self.back_button)

"""    # 自定义一个find_element函数
    def find_element(self, loc):
        # 让系统调用自己的find_element，return返回得到的结果给系统
        return self.driver.find_element(loc[0], loc[1])"""