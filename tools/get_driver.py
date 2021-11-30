# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: get_driver
# @author: kyle
# @date: 2021/10/9 16:34
from selenium import webdriver


class GetDriver:
    __web_driver = None

    # get driver function
    @classmethod
    def get_web_driver(cls, url):
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)
        return cls.__web_driver

    # quit driver function
    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
            cls.__web_driver = None
        pass
