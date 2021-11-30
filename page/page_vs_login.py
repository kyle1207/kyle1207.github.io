# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: ui_vs_login
# @author: kyle
# @date: 2021/10/9 16:02
import allure

import page
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageVsLogin(Base):

    @allure.step("one step")
    def page_input_username(self, username):
        self.base_input(page.vs_username, username)

    @allure.step("two step")
    def page_input_password(self, password):
        self.base_input(page.vs_password, password)

    @allure.step("three step")
    def page_click_login_btn(self):
        self.base_click(page.vs_login_btn)

    @allure.step("four step")
    def page_get_nickname(self):
        return self.base_get_text(page.vs_nickname)

    # about login business to integration
    def page_vs_login(self, username, password):
        log.info("正在调用vStudio登录业务方法，Test账号'用户名为：{}、密码为：{}'".format(username, password))
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
