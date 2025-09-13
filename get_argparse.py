# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/8/12 20:00
@Auth ： IMin--Timo ewei@imin.com
@File ：get_argparse.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""
import argparse
import os

import pytest

import page


class GetArgparse:
    def __init__(self):
        self.parse = argparse.ArgumentParser()

    def add_parameter(self):
        self.parse.add_argument("-dir", "--BASE_PATH", help="项目目录")
        self.parse.add_argument("-id", "--UDID", help="设备的SN号", default=page.udid)
        self.parse.add_argument("-ap", "--APPPACKAGE", default=page.appPackage, help="应用包名")
        self.parse.add_argument("-ac", "--APPACTIVITY", default=page.appActivity, help="应用包名")
        # os.environ["APPPACKAGE"] = self.parse.parse_args().__dict__.get("APPPACKAGE")
        # os.environ["APPACTIVITY"] = self.parse.parse_args().__dict__.get("APPACTIVITY")
        # os.environ["UDID"] = self.parse.parse_args().__dict__.get("UDID")
        return self.parse.parse_args().__dict__


# os.environ["DIRPATH"] = os.getcwd()
# print(os.environ.get("ANDROID_HOME"))
# print(os.environ.values())
if __name__ == '__main__':
    c = GetArgparse()
    par = c.add_parameter()
    print(par)
    # print(os.environ["UDID"])
    print(os.environ)


