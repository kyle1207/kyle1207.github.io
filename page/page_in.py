# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: ui_in
# @author: kyle
# @date: 2021/10/9 15:59
from page.page_vs_login import PageVsLogin
from page.page_vs_file_upload import PageVsFileUpload


class PageIn:

    def __init__(self, driver):
        self.driver = driver

    def page_get_PageVsLogin(self):
        return PageVsLogin(self.driver)

    def page_get_PageVsFileUpload(self):
        return PageVsFileUpload(self.driver)
