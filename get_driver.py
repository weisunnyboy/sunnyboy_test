# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/7/3 15:00
@Auth ： IMin--Timo ewei@imin.com
@File ：get_driver.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""
import os
import socket
import sys
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
from appium.options.common import AppiumOptions
from tools.read_yaml import ReadYaml
import page
from tools.systemic_interaction import SysInter
from tools.get_log import GetLog
import pytest

loger = GetLog.get_logger()
read = ReadYaml("get_driver.yaml")


class GetDriver:
    _app_dirver = None

    @classmethod
    def get_driver(cls):
        """
        :param 读取配置文件get_driver.yaml
        :return: 返回driver
        """
        options = AppiumOptions()
        if cls._app_dirver is None:
            # 重新设置SN的值
            SysInter().get_sn_number()
            loger.info("正在加载驱动driver")
            options.load_capabilities(read.read_yaml())
            cls._app_dirver = webdriver.Remote("http://localhost:4723",
                                               options=options)

        return cls._app_dirver

    @classmethod
    def quit_driver(cls):
        if cls._app_dirver:
            loger.info("正在结束驱动driver")
            cls._app_dirver.quit()
            cls._app_dirver = None

    @classmethod
    def is_port_in_use(cls, port):
        """
        :param port: 端口号，判断端口号是否存在
        :return:
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(("localhost", port)) == 0

    @classmethod
    def run_pytest(cls):
        appium_port = 4723
        if cls.is_port_in_use(appium_port):
            print(f"Appium server is running on port {appium_port}")
        else:
            print(f"Appium server is NOT running on port {appium_port}")
            sys.exit("appium服务没启动，请启动服务再运行")
        pytest.main()


if __name__ == '__main__':
    from base.base import Base

    # from common.setting_config import LOGS_PATH
    #
    # driver = GetDriver.get_driver()
    # logs = driver.get_log("logcat")
    # with open(LOGS_PATH + os.sep + 'logcat_logs.txt', 'w') as file:
    #     for log in logs:
    #         file.write(f"{log}\n")
    # driver.press_keycode(4)
    # actions = ActionChains(driver)
    # element = Base(driver).base_find(page.dd)
    # element1 = Base(driver).base_find(page.dd1)
    # actions.click_and_hold(element).pause(5).perform()
    # time.sleep(10)
    GetDriver.get_driver()
    time.sleep(5)
    GetDriver.quit_driver()
    # appium_port = 4723
    # if GetDriver().is_port_in_use(appium_port):
    #     print(f"Appium server is running on port {appium_port}")
    # else:
    #     print(f"Appium server is NOT running on port {appium_port}")
    #     sys.exit("appium服务没启动，请启动服务再运行")
