# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/7/9 9:31
@Auth ： IMin--Timo ewei@imin.com
@File ：base.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""
import base64
import datetime
import os
import time

from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import page
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from common.setting_config import IMG_PATH

loger = GetLog.get_logger()


class Base:
    def __init__(self, driver):
        """
        :param driver: 获取driver对象
        """
        self.driver = driver

    def base_find(self, loc, timeout=30, poll=0.5):
        try:
            loger.info("Element search~~~loading~~~")
            """
            :param loc: 查找的元素对象
            :param timeout: 查找元素时间
            :param poll: 查找元素频率
            :return: 返回查找元素对象
            """
            if WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc)):
                loger.info(f"~~~~~~~找到元素了{loc}~~~~~~~~")
                return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                    lambda x: x.find_element(*loc))
        except Exception as e:
            loger.error(f"没有找到元素{loc}，请检查元素信息是否存在~~~~~")

    def base_input(self, loc, value):
        """
        :param loc: 查找元素对象
        :param value: 输入的文本信息
        :return:
        """
        loger.info(f"正在调用输入方法，输入的值是{value}")
        e1 = self.base_find(loc)
        e1.clear()
        e1.send_keys(value)

    def base_click(self, loc):
        """
        :param loc: 查找元素对象
        :return:
        """
        loger.info("正在调用点击方法")
        self.base_find(loc).click()

    def base_get_text(self, loc):
        """
        :param loc: 查找元素对象
        :return: 返回元素文本信息
        """
        loger.info("正在调用获取元素文本信息方法")
        return self.base_find(loc).text

    def base_screenshot(self,
                        file_path=IMG_PATH + os.sep + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') + ".png"):
        try:
            self.driver.get_screenshot_as_file(file_path)
            loger.info(f"正在调用截图方法：获取的截图信息保存在：{IMG_PATH}路径下")
        except Exception as e:
            loger.error(f"截图失败 失败信息{e}")

    def base_screen_recording_strat(self):
        try:
            self.driver.start_recording_screen()
            loger.info("正在调用录屏方法，开始录制")
        except Exception as e:
            loger.error(f"录屏失败 失败信息{e}")

    def base_screen_recording_end(self, file_path=IMG_PATH + os.sep + datetime.datetime.now().strftime(
        '%Y-%m-%d-%H-%M') + ".mp4"):
        try:
            sr = self.driver.stop_recording_screen()
            loger.info(f"正在调用录屏方法，结束录制，视频存放在{IMG_PATH}目录下")
            # file_path = IMG_PATH + os.sep + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".mp4"
            with open(file_path, "wb") as f:
                f.write(base64.b64decode(sr))
                # f.write(sr.decode("base64"))
        except Exception as e:
            loger.error(f"视频录制失败 失败信息{e}")

    def base_get_size(self):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        loger.info(f"正在调用获取设备分辨率方法,获取的分辨率为{width}x{height}")
        return self.driver.get_window_size()

    def base_start_app(self, app_package):
        loger.info(f"正在启动打开的应用程序是{app_package}")
        self.driver.activate_app(app_package)

    def base_down_sliding(self, duration=1000):
        """
        :param duration: 间隔时间为毫秒
        :return:
        """
        try:
            loger.info("正在向下滑动")
            sz = self.base_get_size()
            x1 = sz["width"] * 0.5
            y1 = sz["height"] * 0.25
            y2 = sz["height"] * 0.75
            self.driver.swipe(x1, y1, x1, y2, duration=duration)
        except Exception as e:
            loger.error(f"下滑失败 失败原因{e}")

    def base_up_sliding(self, duration=1000):
        try:
            loger.info("正在向上滑滑动")
            sz = self.base_get_size()
            x1 = sz["width"] * 0.5
            y1 = sz["height"] * 0.75
            y2 = sz["height"] * 0.25
            self.driver.swipe(x1, y1, x1, y2, duration=duration)
        except Exception as e:
            loger.error(f"上划失败 错误信息{e}")

    def base_left_sliding(self, duration=1000):
        try:
            loger.info("正在向左滑动")
            sz = self.base_get_size()
            x1 = sz["width"] * 0.75
            y1 = sz["height"] * 0.5
            x2 = sz["width"] * 0.25
            self.driver.swipe(x1, y1, x2, y1, duration=duration)
        except Exception as e:
            loger.error(f"左滑失败 失败信息{e}")

    def base_right_sliding(self, duration=1000):
        try:
            loger.info("正在向右滑动")
            sz = self.base_get_size()
            x1 = sz["width"] * 0.25
            y1 = sz["height"] * 0.5
            x2 = sz["width"] * 0.75
            self.driver.swipe(x1, y1, x2, y1, duration=duration)
        except Exception as e:
            loger.error(f"右滑动失败 失败原因{e}")

    def base_swip_sliding_elements(self, elemnet, direction=None, duration=500):
        """

        :param elemnet: 查找的元素信息
        :param direction:  判断滑动方向  up 向上滑动
        :param duration:  滑动间隔时间   间隔时间为毫秒
        :return:
        """
        ele_sz = self.base_find(elemnet)
        # 获取元素的高
        height = ele_sz.size["height"]
        # 获取元素的宽
        width = ele_sz.size["width"]
        # 获取元素的左上角坐标
        ele_coordinate = ele_sz.location
        # 元素左上角横坐标
        x = ele_coordinate['x']
        # 元素左上角纵坐标
        y = ele_coordinate['y']
        if direction == "up":
            try:
                loger.info("正在向上滑动屏幕")
                # 开始滑动坐标
                start_x = x + width * 0.5
                start_y = (y + height) * 0.80
                # 滑动结束坐标
                end_x = x + width * 0.5
                end_y = (y + height) * 0.20
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=duration)
            except Exception as e:
                loger.error(f"向上滑动失败，失败的原因{e}")
        elif direction == "down":
            try:
                loger.info("正在向下滑动屏幕")
                # 开始滑动坐标
                start_x = x + width * 0.5
                start_y = (y + height) * 0.30
                # 滑动结束坐标
                end_x = x + width * 0.5
                end_y = (y + height) * 0.70
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=duration)
            except Exception as e:
                loger.error(f"向下滑动失败 失败原因 {e}")
        elif direction == "left":
            try:
                loger.info("正在向左滑动屏幕")
                start_x = (x + width) * 0.80
                start_y = height * 0.5 + y
                # 滑动结束坐标
                end_x = (x + width) * 0.20
                end_y = height * 0.5 + y
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=duration)
            except Exception as e:
                loger.error(f"向左滑动失败 失败原因 {e}")
        elif direction == "right":
            try:
                loger.info("正在向右滑动屏幕")
                start_x = (x + width) * 0.20
                start_y = height * 0.5 + y
                # 滑动结束坐标
                end_x = (x + width) * 0.80
                end_y = height * 0.5 + y
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=duration)
            except Exception as e:
                loger.error(f"向右滑动失败 失败原因 {e}")
        else:
            loger.info(f"没有对{elemnet}做滑动操作")

    def base_find_no_log(self, loc, timeout=30, poll=0.5):
        try:
            """
            :param loc: 查找的元素对象
            :param timeout: 查找元素时间
            :param poll: 查找元素频率
            :return: 返回查找元素对象
            :ele : 当el为0的时候元素未找到
            """
            if WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc)):
                return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                    lambda x: x.find_element(*loc))
        except Exception as e:
            loger.error(f"没有找到元素{loc}，请检查元素信息是否存在~~~~~")

    def base_get_text_no_log(self, loc):
        """
        :param loc: 查找元素对象
        :return: 返回元素文本信息
        """
        return self.base_find_no_log(loc).text


if __name__ == '__main__':
    driver = GetDriver.get_driver()
    a = Base(driver)
    time.sleep(20)
    actions = ActionChains(driver)


    # 输入源设备列表为空

    # actions.w3c_actions.devices = []

    # 添加一个新的输入源到设备到中，输入源类型为Touch

    # new_input = actions.w3c_actions.add_pointer_input('touch', 'finger1')
    # new_input1 = actions.w3c_actions.add_pointer_input('touch', 'finger2')
    # new_input2 = actions.w3c_actions.add_pointer_input('touch', 'finger3')
    # new_input3 = actions.w3c_actions.add_pointer_input('touch', 'finger4')
    # new_input4 = actions.w3c_actions.add_pointer_input('touch', 'finger5')

    # data_ley = [["touch", "finger", 655, 328], ["touch", "finger1", 432, 885], ["touch", "finger2", 555, 749],
    #             ["touch", "finger3", 666, 888],
    #             ["touch", "finger4", 444, 335]]

    #
    #

    def base_touch():
        new_input = actions.w3c_actions.add_pointer_input('touch', 'finger1')
        new_input1 = actions.w3c_actions.add_pointer_input('touch', 'finger2')
        new_input2 = actions.w3c_actions.add_pointer_input('touch', 'finger3')
        new_input3 = actions.w3c_actions.add_pointer_input('touch', 'finger4')
        new_input4 = actions.w3c_actions.add_pointer_input('touch', 'finger5')
        new_input.create_pointer_move(x=999, y=612)
        new_input.create_pointer_down()
        new_input.create_pause(0.2)

        new_input1.create_pointer_move(x=585, y=610)
        new_input1.create_pointer_down()
        new_input1.create_pause(0.2)

        new_input2.create_pointer_move(x=987, y=436)
        new_input2.create_pointer_down()
        new_input2.create_pause(0.2)

        new_input3.create_pointer_move(x=790, y=448)
        new_input3.create_pointer_down()
        new_input3.create_pause(0.2)

        new_input4.create_pointer_move(x=586, y=440)
        new_input4.create_pointer_down()
        new_input4.create_pause(0.2)


    # base_touch()
    # actions.perform()
    for i in range(2):
        actions.w3c_actions.pointer_action.move_to_location(x=0, y=33).click_and_hold().move_to_location(0, 752)
        actions.perform()
        actions.w3c_actions.pointer_action.move_to_location(x=0, y=0).click_and_hold().move_to_location(1328, 0)
        actions.w3c_actions.pointer_action.move_to_location(x=0, y=752).click_and_hold().move_to_location(1332, 756)
        actions.w3c_actions.pointer_action.move_to_location(x=0, y=752).click_and_hold().move_to_location(1348, 0)
    base_touch()
    actions.perform()
    # 输入源的动作：移动到某个点，按下，移动到另外一点，释放

    # new_input.create_pointer_move(x=999, y=612)
    # new_input.create_pointer_down()
    # new_input.create_pause(0.2)
    #
    # new_input1.create_pointer_move(x=585, y=610)
    # new_input1.create_pointer_down()
    # new_input1.create_pause(0.2)
    #
    # new_input2.create_pointer_move(x=987, y=436)
    # new_input2.create_pointer_down()
    # new_input2.create_pause(0.2)
    #
    # new_input3.create_pointer_move(x=790, y=448)
    # new_input3.create_pointer_down()
    # new_input3.create_pause(0.2)
    #
    # new_input4.create_pointer_move(x=586, y=440)
    # new_input4.create_pointer_down()
    # new_input4.create_pause(0.2)

# 以此类推，可以添加多个输入源操作到设备当中。可以是鼠标操作，也可以是触屏，按键等操作
