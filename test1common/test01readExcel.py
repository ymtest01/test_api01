#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: YM
@site:
@software: PyCharm
@file: readExcel.py
@time: 2020/5/21 17:16
"""
import xlrd

class ReadExcel():
     def readExcel(fileName,SheetName="Sheet1"):
         data = xlrd.open_workbook(fileName)
         table = data.sheet_by_name(SheetName)

         #获取总行数、总列数
         nrows = table.nrows
         ncols = table.ncols
         if nrows > 1:
             #获取第一列的内容，列表格式
             keys = table.row_values(0)
             #print(keys)

             listApiData = []
             #获取每一行的内容，列表格式
             for col in range(1,nrows):
                 values = table.row_values(col)
                 # keys，values这两个列表一一对应来组合转换为字典
                 api_dict = dict(zip(keys, values))
                 #print(api_dict)
                 listApiData.append(api_dict)

             return listApiData
         else:
             print("表格未填写数据")
             return None

if __name__ == '__main__':

    s = ReadExcel.readExcel("F:/pyCharm脚本文件/unittest学习脚本/练习项目1/test1data/test-ddt1.xlsx","Sheet1")
    print(s)
