#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author:YM
@site:
@software: PyCharm
@file: run_main.py
@time: 2020/5/22 10:58
"""

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
import time
import os
from test1common.HTMLTestRunner_jpg import HTMLTestRunner

def run_case(dir = "test1testcase"):
    case_dir = os.path.dirname(os.getcwd()) + "\\" + dir
    print(case_dir)
    test_case = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test01rulesapi.py",top_level_dir=None)
    return discover


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.dirname(os.getcwd()) + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    fp = open(report_path, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'rules实时规则接口',verbosity=2)
    runner.run(run_case())
    fp.close()