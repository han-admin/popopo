# -*- coding: utf-8 -*-

# 常用的功能都放在这里

class BaceAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    # 自定义一个find_element函数
    def find_element(self, loc):
        # 让系统调用自己的find_element，return返回得到的结果给系统
        return self.driver.find_element(loc[0], loc[1])