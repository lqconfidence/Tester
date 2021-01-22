# -*-coding:utf-8 -*-
# @Time:2020/8/21 10:16
# @Author:a'nan
# @Email:934257271
# @File:test_tag.py

import unittest
import ddt
import requests
import jsonpath
from middleware.ppcrwaler_text import MidPpcrawler
from common.excel_handler import excel_ppcrawler
from common.loger_handler import mylog
import time
import chardet
from learn import local_weight
sheet_name = "tag"
test_datas = excel_ppcrawler.read(sheet_name)

@ddt.ddt
class TestCategorize(unittest.TestCase):
    def setUp(self):
        mylog.info("test start")
        pass

    def tearDown(self):
        mylog.info("test finished")
        pass

    @ddt.data(*test_datas)
    def test_categorize(self, test_data):
        case_id = test_data['case_id']
        cate = test_data['cate']
        weight = test_data['weight']
        tag = test_data['tag']
        print(cate, type(cate), weight, type(weight), tag, type(tag))
        if cate == weight & weight == True:
            pri_result = True
            excel_ppcrawler.write(sheet_name=sheet_name, row=case_id + 1, column=12, data=pri_result)
        else:
            pri_result = False
            excel_ppcrawler.write(sheet_name=sheet_name, row=case_id + 1, column=12, data=pri_result)
        if pri_result == tag:
            excel_ppcrawler.write(sheet_name=sheet_name, row=case_id+1, column=13, data="pass")
        else:
            excel_ppcrawler.write(sheet_name=sheet_name, row=case_id + 1, column=13, data="fail")





