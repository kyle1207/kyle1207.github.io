# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: get_log
# @author: kyle
# @date: 2021/10/11 14:00
import logging.handlers
import os

from config import BASE_PATH


class GetLog:
    __logger = None

    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            cls.__logger = logging.getLogger()
            cls.__logger.setLevel(logging.INFO)
            log_path = BASE_PATH + os.sep + "log" + os.sep + "EXDUITEST.log"
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=1,
                                                           encoding="utf-8")
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d))] - %(message)s"
            fm = logging.Formatter(fmt)
            th.setFormatter(fm)
            cls.__logger.addHandler(th)
        return cls.__logger


if __name__ == '__main__':
    log = GetLog.get_logger()
    log.info("测试信息级别日志")
    log.error("测试错误级别")
