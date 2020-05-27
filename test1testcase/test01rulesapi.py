#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site:
@software: PyCharm
@file: case_01.py
@time: 2018/3/16 10:58
"""
# import sys
# sys.path.append("F:/pyCharm脚本文件/unittest学习脚本/练习项目1/test1common/test01sendRequests")
# sys.path.append("F:/pyCharm脚本文件/unittest学习脚本/练习项目1/test1common/test01readExcel")

# import sys
# import os
# if __name__ == '__main__':
#     sys.path.append(os.path.dirname(sys.path[0]))


import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)



import unittest
import requests
from ddt import ddt,data,unpack
from test1common.test01sendRequests import SendRequests
from test1common.test01readExcel import ReadExcel
import os

# current_directory = os.path.dirname(os.path.abspath(__file__))
# root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
# sys.path.append(root_path)



#print(os.path.dirname(os.getcwd()))
path = os.path.dirname(os.getcwd())+"\\test1data\\test-ddt1.xlsx"
print(path)
testData = ReadExcel.readExcel(path,"Sheet1")

@ddt
class Test1(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @data(*testData)
    def test_rlue_api(self,data):

        re = SendRequests().sendRequests(self.s, data)
        #print(re.json())

        #切割字符串取后面的部分
        expect_result1 = data["预期结果"].split(":")[1]
        #转换为字符串
        expect_result = eval(expect_result1)
        #print(expect_result)

        self.assertEqual(re.json()["eval_code"], expect_result, "返回错误,实际结果是%s"%re.json()["eval_code"])


if __name__ == '__main__':
    unittest.main()