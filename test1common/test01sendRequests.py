# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: YM
@site:
@software: PyCharm
@file: sendRequests.py
@time: 2020/5/24 11:40
"""
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)



#from test01readExcel import ReadExcel
from test1common.test01readExcel import ReadExcel
import requests
import json



class SendRequests():

    def sendRequests(self,s,apiData):

        '''
                从读取的表格中获取响应的参数作为传递
                '''
        # try:
        #     method = apiData["method"]
        #     url = apiData["url"]
        #     if apiData["params"] == "":
        #         par = None
        #     else:
        #         par = eval(apiData["params"])
        #
        #     if apiData["headers"] == "":
        #         h = None
        #     else:
        #         h = apiData["headers"]
        #
        #     if apiData["body"] == "":
        #         body_data = None
        #     else:
        #         body_data = eval(apiData["body"])
        #
        #     type = apiData["type"]
        #     v = False
        #     if type == "json":
        #         body = json.dumps(body_data)
        #     if type == "data":
        #         body = body_data
        #     else:
        #         body = body_data
        #
        #     #发送请求
        #     re = s.request(method=method,url=url,headers=h,params=par,data=body,verify=v)
        #     return re
        #
        # except Exception as e:
        #     print(e)

        method = apiData["接口请求方法"]
        url = apiData["接口地址"]
        if apiData["参数"] == "":
            par = None
        else:
            par = eval(apiData["参数"])

        if apiData["请求头"] == "":
            h = None
        else:
            h = eval(apiData["请求头"])

        if apiData["输入数据"] == "":
            body_data = None
            # body = None
        else:
            body_data = eval(apiData["输入数据"])
            # body = json.dumps(body_data)

            # print(body)
            datatype = apiData["数据类型"]

            if datatype == "data":
                body = body_data
            elif datatype == "json":
                body = json.dumps(body_data)

            else:
                body = body_data


        v = False

        # if datatype =="json":
        #     body = json.dumps(body_data)
        #     print(body)
        # if datatype == "data":
        #     body = body_data
        #
        # else:
        #     body = body_data

        # 发送请求
        re = s.request(method=method, url=url, headers=h, params=par, data=body, verify=v)
        return re

if __name__ == '__main__':
    s = requests.session()
    testData = ReadExcel.readExcel("F:/pyCharm脚本文件/unittest学习脚本/练习项目1/test1data/test-ddt1.xlsx", "Sheet1")
    # print(testData[0])
    response = SendRequests().sendRequests(s,testData[0])
    d=json.dumps(response.json())
    print(response.json())


