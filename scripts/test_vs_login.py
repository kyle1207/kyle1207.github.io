# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: test_vs_login
# @author: kyle
# @date: 2021/10/9 16:32
import page
import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestVsLogin:

    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_vs)
        self.vs = PageIn(driver).page_get_PageVsLogin()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,password,expect", read_yaml("vs_login.yaml"))
    def test_vs_login(self, username, password, expect):
        self.vs.page_vs_login(username, password)
        print("The nickname obtained is:", self.vs.page_get_nickname())
        process_before = self.vs.page_get_nickname()
        process_later = process_before.strip()
        try:
            assert expect == process_later
        except Exception as e:
            log.error("断言出错，错误信息：{}".format(e))
            print("断言出错，错误信息：", e)
            self.vs.base_get_img()
            raise
