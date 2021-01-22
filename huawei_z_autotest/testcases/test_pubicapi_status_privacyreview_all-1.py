# -*-coding:utf-8 -*-
# @Time:2020/7/27 10:35
# @Author:a'nan
# @Email:934257271
# @File:test_pubicapi_status_prv.py

import unittest
import ddt
from common.loger_handler import mylog
import json
import requests
import time
import jsonpath

from common.excel_handler import excel_hw_privacyreview_all

from common.sheet_header import SheetHeader

from common.excel_handler import excel_hw_privacyreview_case

from common.sheet_header import SheetHeader

sheet_name = "privacyreview"
head_data = excel_hw_privacyreview_case.header(sheet_name)
sheet_head = SheetHeader(head_data)
#sheet_column = sheet_head.__dict__
#print("-----------------------sheet_head类型为{}---值为{}".format(type(sheet_head),sheet_head.__dict__))
test_datas = excel_hw_privacyreview_case.read(sheet_name)

@ddt.ddt
class TestPrivacyReview1(unittest.TestCase):

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_datas)
    def test_hw_pp1(self, test_data):
        mylog.info('test data{}'.format(test_data))

        method = "POST"
        trace_id = test_data['trace_id']


        # 请求参数
        request_body = {    "request":[        {           "task_id":trace_id,         "type": ["secret"]        }    ]}
        res = None
        url = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/status?tpl=hw-z-p'
        headers = {'X-HOST': 'hwa-grayapp.avlyun.com', 'X-PORT': '80', 'X-SK': 'testtest',
                   'Content-Type': 'application/json'}
        if method.upper() == 'GET':
            try:
                mylog.info("url=====" + url)
                res = requests.get(url=url, params=None, cookies=None)
            except Exception as e:
                mylog.error('request -get error the reason is {}'.format(e))
        elif method.upper() == 'POST':
            try:
                mylog.info("url=====" + url)
                mylog.info("data_json==")
                mylog.info(request_body)
                res = requests.post(url=url, data=None, json=request_body, cookies=None, headers=headers)
                #print(res.json())
            except Exception as e:
                mylog.error('request -post error the reason is {}'.format(e))
        else:
            mylog.error('request method error')
        secret_result = jsonpath.jsonpath(res.json(), "$..secret_result")[0]
        prv_is_privacy = jsonpath.jsonpath(secret_result,'$..prv_is_privacy')[0]
        #print(type(secret_result),secret_result)
        secret_err_msg = jsonpath.jsonpath(secret_result, "$..err_msg")[0]
        secret_err_code = jsonpath.jsonpath(secret_result, "$..err_code")[0]
        prv_policy_content = jsonpath.jsonpath(secret_result, "$..prv_policy_content")[0]

        #mylog.info('test result{}'.format(res.text))
        # for i in secret_result.keys():
        #     print("*********这是secret的key值"+i+"********")
        #     i = jsonpath.jsonpath(secret_result, "$..{}".format(i))[0]
        #     #li是secret_result所有key的value
        #     li.append(i)
        # print("#####################secretresult的所有key",li)
        # for j in secret_result.keys():
        #     ji.append(j)

        #excel_ppcrawler.write(sheet_name, test_data['case_id'] + 1, 7, secret_err_code)
        #excel_ppcrawler.write(sheet_name, test_data['case_id'] + 1, 8, secret_err_msg)
        excel_hw_privacyreview_all.write(sheet_name, test_data['case_id'] + 1,
                                    sheet_head.__getattribute__("prv_is_privacy"),str(prv_is_privacy))
        excel_hw_privacyreview_all.write(sheet_name, test_data['case_id'] + 1,
                                    sheet_head.__getattribute__("err_msg"), str(secret_err_msg))
        excel_hw_privacyreview_all.write(sheet_name, test_data['case_id'] + 1,
                                    sheet_head.__getattribute__("err_code"), str(secret_err_code))
        prv_policy_content_data = prv_policy_content["data"]
        for i in  prv_policy_content_data:
            excel_hw_privacyreview_all.write(sheet_name, test_data['case_id'] + 1, sheet_head.__getattribute__(i["type"]),
                                  "state:{}".format( i["state"])+"--data:{}".format(str(i["data"])))




if __name__ == '__main__':
    unittest.main()
