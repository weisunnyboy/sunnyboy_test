# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/7/24 10:26
@Auth ： IMin--Timo ewei@imin.com
@File ：run_therading.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""
import threading
from tools.get_log import GetLog

logger = GetLog.get_logger()


class RunTherading():
    """
    开启多线程
    """
    def __init__(self, function_name):
        self.rt = None
        self.function_name = function_name

    def run_therading(self):
        if self.function_name:
            self.rt = threading.Thread(target=self.function_name)
            logger.info(
                f"~~~启动多线程任务 线程名:{threading.current_thread().name} 正在运行线程数量{threading.active_count()} ")
            self.rt.daemon = True  # 守护线程将在主线程退出时自动终止
            self.rt.start()
        else:
            logger.error("多线程任务启动失败")
