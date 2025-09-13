# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/9/3 9:47
@Auth ： IMin--Timo ewei@imin.com
@File ：test_14mmitest.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""
import os
import time

import page
from tools.get_driver import GetDriver
from page.page_in import PageMmiTest
from tools.get_log import GetLog
import datetime
import allure
from common.setting_config import IMG_PATH

logger = GetLog.get_logger()


class TestMmiTest:
    def setup_class(self):
        driver = GetDriver.get_driver()
        self.page_in = PageMmiTest(driver)

    @allure.feature("MMItest--主板测试")
    @allure.story("主板自动测试")
    @allure.title("主板自动测试成功")
    def test_01_board_auto_test(self):
        # mmi主板自动测试
        try:
            if self.page_in.page_board_auto_test() is True:
                assert self.page_in.base_find(page.mmi_test_result_ewm, timeout=3)
                logger.info("主板自动测试用例pass")
        except Exception as e:
            logger.error("主板自动测试执行失败fail")
            self.page_in.base_screen_recording_end(file_path=IMG_PATH + os.sep + datetime.datetime.now().strftime(
                '%Y-%m-%d-%H-%M') + "主板测试--主板自动测试.mp4")
            print(e)
            raise e

    @allure.feature("MMItest--主板测试")
    @allure.story("主板手动测试")
    @allure.title("主板手动测试成功")
    def test_02_board_artificial_test(self):
        # mmi主板手动测试
        try:
            if self.page_in.page_board_artificial_test() is True:
                assert self.page_in.base_find(page.mmi_quit, timeout=3) and self.page_in.base_find(page.mmi_number25,
                                                                                                   timeout=3)
                logger.info("主板手动测试用例pass")
        except Exception as e:
            logger.error("主板手动测试执行失败fail")
            self.page_in.base_screen_recording_end(file_path=IMG_PATH + os.sep + datetime.datetime.now().strftime(
                '%Y-%m-%d-%H-%M') + "主板测试--主板手动测试.mp4")
            print(e)
            raise e

    @allure.feature("MMItest--整机测试")
    @allure.story("整机手动测试")
    @allure.title("整机手动测试成功")
    def test_03_whole_artificial_test(self):
        # mmi整机手动测试
        try:
            if self.page_in.page_board_artificial_test() is True:
                assert self.page_in.base_find(page.mmi_quit, timeout=3) and self.page_in.base_find(page.mmi_number53,
                                                                                                   timeout=3)
                logger.info("整机手动测试用例pass")
        except Exception as e:
            logger.error("整机手动测试执行失败fail")
            self.page_in.base_screen_recording_end(file_path=IMG_PATH + os.sep + datetime.datetime.now().strftime(
                '%Y-%m-%d-%H-%M') + "整机测试--整机手动测试.mp4")
            print(e)
            raise e

    @allure.feature("MMItest--整机测试")
    @allure.story("整机自动测试测试")
    @allure.title("自动测试成功")
    def test_04_whole_auto_test(self):
        # mmi整机自动测试
        try:
            if self.page_in.page_whole_aotu_test() is True:
                assert self.page_in.base_find(page.mmi_number89, timeout=3)
                logger.info("整机自动测试用例pass")
        except Exception as e:
            logger.error("整机自动测试执行失败fail")
            self.page_in.base_screen_recording_end(file_path=IMG_PATH + os.sep + datetime.datetime.now().strftime(
                '%Y-%m-%d-%H-%M') + "整机测试--整机自动测试.mp4")
            print(e)
            raise e

    def teardown_class(self):
        time.sleep(5)
        GetDriver.quit_driver()
