# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: test_vs_file_upload
# @author: kyle
# @date: 2021/10/15 10:44
import pytest
import page

from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestVsFileUpload:
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_vs)
        driverF = GetDriver.get_web_driver(page.url_vs_fileupload)
        self.vs = PageIn(driver).page_get_PageVsLogin()
        self.vs.file = PageIn(driverF).page_get_PageVsFileUpload()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,password", read_yaml("vs_file_upload.yaml"))
    def test_vs_file_upload(self, username, password):
        from tools.read_yaml import read_yaml
        self.vs.page_vs_login(username, password)
        self.vs.file.page_vs_file_upload()
        self.vs.file.page_get_filename()
        print("文件名称为", self.vs.file.page_get_filename())
        getFileName = self.vs.file.page_get_filename()
        f = read_yaml("vs_upload_file_info.yaml")
        res = f[0][1]
        try:
            assert getFileName == res
            print("新上传的文件名称为：", self.vs.file.page_get_filename())
        except Exception as e:
            log.error("断言出错，错误信息：{}".format(e))
            print("断言出错，错误信息：", e)
            self.vs.base_get_img()
            raise
