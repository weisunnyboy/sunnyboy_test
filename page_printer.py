# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/8/8 16:31
@Auth ： IMin--Timo ewei@imin.com
@File ：page_printer.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""
import page
from base.base import Base
from tools.get_log import GetLog

logger = GetLog.get_logger()


class PagePrinter(Base):
    def page_printer(self):
        logger.info("打开单项检测-打印机")
        self.base_screen_recording_strat()
        self.base_click(page.dyj)
        self.base_click(page.d_sx)
        self.base_click(page.d_ckbz)
        self.base_click(page.d_qpd)
        self.driver.press_keycode(4)

    def page_printer_usb_exist(self):
        logger.info("有USB外设打印机设备时候，打印机打印")
        self.base_screen_recording_strat()
        self.base_click(page.d_sx)
        self.base_click(page.d_ckxqjt)
        self.base_click(page.d_gb)
        self.base_click(page.d_usbdycs)

    def page_printer_ly_exist(self):
        logger.info("连接蓝牙打印机设备打印")
        self.base_screen_recording_strat()
        if self.base_get_text(page.d_ljts) == "1":
            self.base_click(page.d_usbdycs)
        else:
            self.base_click(page.d_lydyce)
