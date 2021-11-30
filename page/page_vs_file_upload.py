# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: page_vs_file_upload
# @author: kyle
# @date: 2021/10/18 9:50

from pywinauto.keyboard import send_keys
from pywinauto import Desktop

import page
from base.base import Base


class PageVsFileUpload(Base):

    def page_click_manage_btn(self):
        self.base_click(page.vs_manage_btn)

    def page_click_upload_btn(self):
        self.base_click(page.vs_upload_btn)

    def page_click_choose_btn(self):
        self.base_click(page.vs_choose_btn)

    def page_click_sure_btn(self):
        self.base_click(page.vs_filesure)

    """
    update on Wed Nov 29 12:23:34 2021
    @author: kyle
    """
    # des: Used as a selection function for uploading files
    def page_vs_file_choose(self):
        from tools.read_yaml import read_yaml
        f = read_yaml("vs_upload_file_info.yaml")
        app = Desktop()
        win = app["打开"]
        # win.print_ctrl_ids()
        win["Toolbar3"].click()
        # send_keys(filenamePat)
        send_keys(f[0][0])
        send_keys("{VK_RETURN}")
        win["文件名(&N):Edit"].type_keys(f[0][1])
        win["打开(&O)"].click()
        self.page_click_sure_btn()

    def page_get_filename(self):
        return self.base_get_text(page.vs_assert_upload)

    def page_vs_file_upload(self):
        self.page_click_manage_btn()
        self.page_click_upload_btn()
        self.page_click_choose_btn()
        self.page_vs_file_choose()
