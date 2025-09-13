# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/7/23 9:37
@Auth ： IMin--Timo ewei@imin.com
@File ：run.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""

from tools.get_log import GetLog

logger = GetLog.get_logger()
from tools.systemic_interaction import SysInter
from tools.get_driver import GetDriver
from tools.run_therading import RunTherading

if __name__ == '__main__':
    # SysInter().clear_logcat()
    # RunTherading(SysInter().run_logcat).run_therading()
    # 自动启动appuim服务
    # appium_service = SysInter().start_appium_server()
    GetDriver.run_pytest()
    SysInter().generate_allure_report()
    # 脚本运行完自动停止APPUIM服务
    # SysInter().stop_appium_server(appium_service)
    # SysInter().stop_logcat()

    # cmd = "adb logcat -c"
    # cmd1 = "adb logcat -v time > ./logs/test123.log"
    # SysInter(cmd).sys_interactive()
    # tt = threading.Thread(target=SysInter(cmd1).sys_interactive)
    # tt.start()
    # pytest.main()
    # cmd2 = "allure generate ./temps -o ./report --clean"
    # SysInter(cmd2).sys_interactive()
    # cmd3 = "adb kill-server"
    # SysInter(cmd3).sys_interactive()
