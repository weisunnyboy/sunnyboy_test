# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/7/3 16:01
@Auth ： IMin--Timo ewei@imin.com
@File ：get_log.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""
import datetime
import os
import logging.handlers
from common.setting_config import LOGS_PATH


# ('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# '%(asctime)s %(levelname)s [%(filename)s(%(funcName)s: %(lineno)d)] - %(message)s'


class GetLog:
    # 新建一个日志器变量
    __logger = None

    # 新建获取日志器的方法
    @classmethod
    def get_logger(cls):
        # 判断日志器是否为空
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 修改默认级别
            cls.__logger.setLevel(logging.INFO)
            # 获取处理器  输出到文件
            file_path = LOGS_PATH+os.sep + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + "log.log"
            th = logging.handlers.TimedRotatingFileHandler(filename=file_path,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=3, encoding="utf-8")
            # 获取格式器
            fmt = '%(asctime)s %(levelname)s [%(filename)s(%(funcName)s: %(lineno)d)] - %(message)s'
            # 获取控制台处理器 输出到控制台
            stream_handler = logging.StreamHandler()

            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            stream_handler.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)
            cls.__logger.addHandler(stream_handler)
        return cls.__logger


if __name__ == '__main__':
    log = GetLog().get_logger()
    log.info("asdsad")
