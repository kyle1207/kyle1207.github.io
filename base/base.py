# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: base
# @author: kyle
# @date: 2021/10/9 13:30
import allure
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import GetLog

log = GetLog.get_logger()


class Base:

    # initialize driver
    def __init__(self, driver):
        log.info("正在初始化driver：{}".format(driver))
        self.driver = driver

    # Encapsulated find function
    def base_find(self, loc, timeout=30, poll=0.3):
        '''
        :param loc: 元素（数据结构为列表或者元组）
        :param timeout: 超时时间，默认30
        :param poll: 步频，默认0.5
        :return: 元素
        '''
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # Encapsulated input function
    def base_input(self, loc, value):
        '''
        :param loc: 元素（数据结构为列表或者元组）
        :param value: 输入值
        '''
        ele = self.base_find(loc)
        log.info("正在清空：{}元素内容".format(loc))
        ele.clear()
        log.info("正在对：{}元素执行输入：{}操作".format(loc, value))
        ele.send_keys(value)

    # Encapsulated click function
    def base_click(self, loc):
        '''
        :param loc: 元素（数据结构为列表或者元组）
        '''
        log.info("正在对: {} 元素进行点击操作".format(loc))
        self.base_find(loc).click()

    # Encapsulated get text function
    def base_get_text(self, loc):
        '''
        :param loc: 元素（数据结构为列表或者元组）
        :return:
        '''
        log.info("正在获取: {} 元素的文本值！获取的文本值为：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text
        # a = self.base_find(loc).text
        # print(a)

    # Encapsulated screenshot function
    def base_get_img(self):
        log.error("断言错误，正在进行截图操作...")
        self.driver.get_screenshot_as_file("./image/err.png")
        log.error("断言出错，正在将截取的错误图片写入Allure报告中")
        self.__base_write_img()

    # The function will write image to report
    def __base_write_img(self):
        with open("./image/err.png", "rb") as f:
            allure.attach(f.read(), "Error cause", allure.attachment_type.PNG)
