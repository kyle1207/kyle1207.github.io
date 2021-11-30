# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: readyamlfile
# @author: kyle
# @date: 2021/11/29 17:49
from tools.read_yaml import read_yaml

f = read_yaml("vs_upload_file_info.yaml")
print(type(f))
print(f)
print(type(f[0][0]))
print(f[0][0])