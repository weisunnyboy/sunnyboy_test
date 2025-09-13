# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/7/23 16:00
@Auth ： IMin--Timo ewei@imin.com
@File ：systemic_interaction.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""
import datetime
import os
import subprocess
import sys
import time
import re
import pytest
from appium.webdriver.appium_service import AppiumService

from common.setting_config import LOGS_PATH
from common.setting_config import REPORT_PATH
from common.setting_config import TEMPS_PATH
from tools.get_log import GetLog
# from tools.get_driver import GetDriver
import page
from tools.read_yaml import ReadYaml

read = ReadYaml("get_driver.yaml")
logger = GetLog.get_logger()


class SysInter:

    def __init__(self, cmds=None):
        self.cmds = cmds

    def sys_interactive(self, result="no"):
        # 与系统交互
        """
        :param result: 如果为ok的话，就打印cmd控制台输出结果
        :return:
        """
        try:
            logger.info(f"正在执行ADB命令，输入的命令是{self.cmds}")
            su = subprocess.Popen(self.cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            ps, er = su.communicate()
            # str_data = []
            if result == "ok":
                # logger.info(ps.decode("gbk"))
                # logger.info(er.decode("gbk"))
                # str_data.append(ps.decode("gbk"))
                # str_data.append(er.decode("gbk"))
                return ps.decode("gbk")
            logger.info(f"{self.cmds} 命令执行成功")
            return su
        except Exception as e:
            logger.error(f"执行cmd命令失败，失败的原因是{e}")

    def generate_allure_report(self, source_dir=TEMPS_PATH, report_dir=REPORT_PATH):
        # 生成allure测试报告
        """
        :param source_dir:  临时文件存放路径
        :param report_dir: allure测试报告存放地址
        :return:
        """
        try:
            logger.info("生成allure报告")
            self.cmds = f"allure generate {source_dir} -o {report_dir} --clean"
            self.sys_interactive()
            logger.info(f"allure报告生成成功，报告路径：{report_dir}")
        except Exception as e:
            logger.error(f"报告生成失败，原因{e}")

    # def run_pytest(self):
    #     appium_port = 4723
    #     if GetDriver().is_port_in_use(appium_port):
    #         print(f"Appium server is running on port {appium_port}")
    #     else:
    #         print(f"Appium server is NOT running on port {appium_port}")
    #         sys.exit("appium服务没启动，请启动服务再运行")
    #     pytest.main()

    def run_logcat(self):
        # 抓取系统日志
        try:
            logger.info("正在抓取系统测试日志")
            file_path = LOGS_PATH + os.sep + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + "syslog.log"
            self.cmds = f"adb logcat -v time > {file_path}"
            self.sys_interactive()
            logger.info(f"抓取的日志文件保存在~~~{LOGS_PATH}目录")
        except Exception as e:
            logger.error(f"抓取系统日志失败 失败原因{e}")

    def stop_logcat(self):
        # 杀死adb服务进程
        try:
            logger.info("正在杀死adb进程")
            self.cmds = "adb kill-server"
            self.sys_interactive()
            logger.info("杀死adb进程成功")
        except Exception as e:
            logger.error(f"杀死ADB进程失败 失败原因{e}")

    def clear_logcat(self):
        # 清除缓存adb缓存日志
        self.cmds = "adb logcat -c"
        self.sys_interactive()

    def devices(self):
        self.cmds = "adb devices"
        self.sys_interactive()

    def start_app(self, package, activity):
        """
        :param package: 应用包名
        :param activity: 启动名
        :return:
        """
        self.cmds = f"adb shell am start -n {package}/{activity}"
        self.sys_interactive()

    def kill_app(self, package):
        self.cmds = f"adb shell am force-stop {package}"
        self.sys_interactive()

    def start_appium_server(self):
        # 创建 Appium 服务实例
        appium_service = AppiumService()
        # 启动 Appium 服务
        appium_service.start(args=['--address', '127.0.0.1', '--port', '4723'])
        logger.info("appium服务自动启动中请稍等~~~~~")
        time.sleep(10)  # 等待 Appium 完全启动
        if appium_service.is_running:
            logger.info("Appium 服务已启动")
        else:
            logger.error("无法启动 Appium 服务")
        return appium_service

    def stop_appium_server(self, appium_service):
        # 停止 Appium 服务
        appium_service.stop()
        if not appium_service.is_running:
            logger.info("Appium 服务已停止")
        else:
            logger.error("无法停止 Appium 服务")

    def file_exits(self, file_path, project=None):
        # 判断文件是否存在
        self.cmds = f"adb shell ls /{file_path}"
        data = self.sys_interactive(result="ok")
        no_file = ""
        pass

    def get_sn_number(self):
        """
        :return: 返回get_driver.yaml内容
        """
        self.cmds = "adb devices"
        data = self.sys_interactive(result="ok")
        try:
            match = re.search(r'([A-Z0-9]{17})', data)
            if match:
                device_id = match.group(1)
                logger.info(f"设备sn:{device_id}")
                # 将get_driver.yaml文件的udid替换成获取设备的ID
                data = read.read_yaml()
                data["udid"] = device_id
                data["deviceName"] = device_id
                read.write_yaml(data)
                return read.read_yaml()
            else:
                sys.exit("请检查设备和电脑是否连接USB成功")
        except:
            match1 = re.search(r'(\d+\.\d+\.\d+\.\d+:\d+)', data)
            if match1:
                device_id = match1.group(1)
                logger.info(f"设备sn:{device_id}")
                # 将get_driver.yaml文件的udid替换成获取设备的ID
                data = read.read_yaml()
                data["udid"] = device_id
                data["deviceName"] = device_id
                read.write_yaml(data)
                return read.read_yaml()
            else:
                sys.exit("请检查设备和电脑是否连接USB成功")

    def get_devices_type(self):
        """

        :return: 返回设备机型，如果有persist.sys.neo_model属性能得到就获取，否词提取SN号
        """
        self.cmds = "adb shell getprop | findstr persist.sys.neo_model"
        data = self.sys_interactive(result="ok")
        match = re.search(r'\[([^\]]+)\]\s*:\s*\[([^\]]+)\]', data)
        if match:
            result = match.group(2)
            project = ["DS2", "ML1"]
            if result in project:
                self.cmds = "adb shell getprop | findstr persist.sys.imin.sn"
                data1 = self.sys_interactive(result="ok")
                match1 = re.search(r"\[N([A-Z0-9]{5})", data1)
                if match1:
                    result1 = match1.group(1)
                    return result1
                else:
                    logger.error("没找到项目名称")
            return result
        else:
            self.cmds = "adb shell getprop | findstr persist.sys.imin.sn"
            data = self.sys_interactive(result="ok")
            match = re.search(r"\[([A-Z0-9]{6,})\]", data)
            if match:
                full_value = match.group(1)
                result = full_value[1:6]
                return result
            else:
                logger.error("无法识别设备机型")


if __name__ == '__main__':
    c = SysInter().get_devices_type()
    print(c)

    # SysInter().start_app(package="com.android.calculator2", activity=".Calculator")
