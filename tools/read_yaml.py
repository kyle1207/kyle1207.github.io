# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: read_yaml
# @author: kyle
# @date: 2021/10/9 16:54
import os

import yaml
from config import BASE_PATH


def read_yaml(filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    # print(file_path)
    # Define empty lists - Assemble test data
    arr = []
    with open(file_path, "r", encoding="utf-8") as f:
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
    return arr


if __name__ == '__main__':
    print(read_yaml("vs_login.yaml"))
    # print(read_yaml("vs_login.yaml").[0])
