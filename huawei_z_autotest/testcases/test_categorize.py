# -*-coding:utf-8 -*-
# @Time:2020/8/12 11:53
# @Author:a'nan
# @Email:934257271
# @File:test_categorize.py
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
sheet_name = "hw_privacyurl"
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
        privacy_url = test_data['privacyUrl']
        ppcrawler_text = MidPpcrawler.Ppcrawler(privacy_url)
        #tag = test_data['tag']
        mylog.info(ppcrawler_text)
        print("爬虫结果类型为{}".format(type(ppcrawler_text)))  #应该是str
        print("转换为encodeutf8之后的类型为{}".format(type(ppcrawler_text.encode('utf-8'))))   #应该是byte
        #print(chardet.detect(ppcrawler_text))
        #print(chardet.detect(ppcrawler_text.encode('utf-8')))
        case_id = test_data['case_id']
        url_cate = 'http://privacy-bayesian-classifier.test.k8ss.cc/v1/categorize'
        url_weight = 'http://privacy-bayesian-classifier.test.k8ss.cc/v1/sample-weight'
        categorize = requests.post(url=url_cate, data=ppcrawler_text.encode('utf-8'))
        print("categorize响应{}".format(categorize.json()))
        weight = requests.post(url=url_weight, data=ppcrawler_text.encode('utf-8'))
        #weight1 = requests.post(url=url_weight, json=ppcrawler_text)
        #weight = requests.post(url=url_weight, json=ppcrawler_text.encode('utf-8'))
        print("weight响应{}".format(weight.json()))
        #print("weight1响应{}".format(weight1.json()))

        # if ppcrawler_text == ppcrawler_text.encode('utf-8'):
        #     print("转换为utf8前后一致")
        # else:
        #     print("转换为utf8前后不一致")
        #local_result = local_weight.local_weigth_test(ppcrawler_text)
        res_cate_data = jsonpath.jsonpath(categorize.json(), "$..data")[0][0]
        print("cate的data值为{}".format(res_cate_data),"类型为{}".format(type(res_cate_data)))
        res_weight = jsonpath.jsonpath(weight.json(), "$..data")[0]
        res_cate = res_cate_data["category"]
        result = "fail"
        try:
            #self.assertEqual(tag, res_weight)
            result = "pass"
        except Exception as e:
            result = 'fail'
            raise e
        finally:
            excel_ppcrawler.write(sheet_name=sheet_name, row=case_id + 1, column=4, data=res_cate)
            excel_ppcrawler.write(sheet_name=sheet_name, row=case_id + 1, column=5, data=categorize.text)
            excel_ppcrawler.write(sheet_name=sheet_name, row=case_id + 1, column=6, data=res_weight)
            excel_ppcrawler.write(sheet_name=sheet_name, row=case_id + 1, column=7, data=weight.text)
            #excel_ppcrawler.write(sheet_name=sheet_name, row=case_id + 1, column=8, data=local_result)

        time.sleep(60)




