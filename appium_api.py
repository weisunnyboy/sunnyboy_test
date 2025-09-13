# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/7/22 21:03
@Auth ： IMin--Timo ewei@imin.com
@File ：appium_api.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""


class AppiumApi:
    def __init__(self, driver):
        self.driver = driver

    def api_back(self):
        # 返回键
        self.driver.press_keycode(4)

    def api_home(self):
        # 回到桌面
        self.driver.press_keycode(3)

    def api_install_app(self, app_path):
        # 安装app
        self.driver.install_app(app_path)

    def api_unstall_app(self, app_name):
        # 卸载APP
        self.driver.remove_app(app_name)

    def api_start_app(self):
        self.driver.launch_app()

    def api_close_app(self):
        self.driver.close_app()
