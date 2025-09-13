# -*- coding: utf-8 -*-
"""
@Company :  IMin
@Time ： 2024/7/3 16:00
@Auth ： IMin--Timo ewei@imin.com
@File ：read_yaml.py
@IDE ：PyCharm
@Motto: IMin--AutoTest
"""
import yaml
import os
import sys
from common.setting_config import DATA_PATH


class ReadYaml:
    def __init__(self, filename):
        self.filename = DATA_PATH + os.sep + filename
        self.__yaml = None

    def read_yaml(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.__yaml = yaml.safe_load(f)
                return self.__yaml
        else:
            raise FileExistsError(f"{self.filename}文件不存在，请检查文件")

    def write_yaml(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            self.__yaml = yaml.safe_dump(data, f, allow_unicode=True)
            return self.__yaml


if __name__ == '__main__':
    read = ReadYaml("get_driver.yaml").read_yaml()
    reads = ReadYaml("counter.yaml").read_yaml()
    # write = ReadYaml("test_05.yaml").write_yaml({"name": "xiaohong", "page": "abcd"})
    print(read)
    print(reads["DS2"])
