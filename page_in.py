# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/7/22 20:33
@Auth ： IMin--Timo ewei@imin.com
@File ：page_in.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""
from page.equipment_manager.page_audio import PageAudio
from page.equipment_manager.page_cashbox import PageCashBox
from page.equipment_manager.page_hardware_test import PageHarTest
from page.equipment_manager.page_network import PageNetWork
from page.equipment_manager.page_scan_code import PageScanCode
from page.equipment_manager.page_show_touch import PageShowTouch
from page.equipment_manager.page_storage import PageStorage
from page.equipment_manager.page_usb import PageUsb
from page.equipment_manager.page_printer import PagePrinter
from page.application_store.page_recommend import PageRecommend
from page.application_store.page_classify import PageClassify
from page.application_store.page_user_guide import PageUserGuide
from page.application_store.page_log import PageLog
from page.application_store.page_mmi_master_test import PageMmiTest


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    def page_get_hardware_test(self):
        return PageHarTest(self.driver)

    def page_get_storage(self):
        return PageStorage(self.driver)

    def page_get_usb_devices(self):
        return PageUsb(self.driver)

    def page_get_network(self):
        return PageNetWork(self.driver)

    def page_get_printer(self):
        return PagePrinter(self.driver)

    def page_get_scan_code(self):
        return PageScanCode(self.driver)

    def page_get_cashbox(self):
        return PageCashBox(self.driver)

    def page_get_show_touch(self):
        return PageShowTouch(self.driver)

    def page_get_audio(self):
        return PageAudio(self.driver)

    def page_get_recommend(self):
        return PageRecommend(self.driver)

    def page_get_classify(self):
        return PageClassify(self.driver)

    def page_get_userguide(self):
        return PageUserGuide(self.driver)

    def page_get_log(self):
        return PageLog(self.driver)

    def page_get_mmitest(self):
        return PageMmiTest(self.driver)
