# -*-coding:utf-8 -*-
# @Time:2020/8/3 9:31
# @Author:a'nan
# @Email:934257271
# @File:test_publicapi_status_bev.py

import unittest
import ddt
from common.loger_handler import mylog
import json
import requests
import time
import jsonpath

from common.excel_handler import excel_analog

from common.sheet_header import SheetHeader

sheet_name = "inspection"
head_data = excel_analog.header(sheet_name)
sheet_head = SheetHeader(head_data)
#sheet_column = sheet_head.__dict__
print("-----------------------sheet_head类型为{}---值为{}".format(type(sheet_head),sheet_head.__dict__))
test_datas = excel_analog.read(sheet_name)

@ddt.ddt
class TestStatusAll(unittest.TestCase):

    def setUp(self):
        mylog.info('test starting')
        pass

    def tearDown(self):
        mylog.info('test finished')
        pass

    @ddt.data(*test_datas)
    def test_status_all11(self, test_data):
        #mylog.info('test data{}'.format(test_data))
        li = []
        ji = []
        method = "POST"
        task_id = test_data['task_id']
        # 请求参数
        request_body = {"request": [{"task_id": task_id, "type": ["secret", "conformance"]}]}
        res = None
        url = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/status?tpl=hw-z-p'
        headers = {'X-HOST': 'public-api.d.k8ss.cc', 'X-PORT': '80', 'X-SK': 'testtest',
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
                print(res.json())
            except Exception as e:
                mylog.error('request -post error the reason is {}'.format(e))
        else:
            mylog.error('request method error')
        secret_result = jsonpath.jsonpath(res.json(), "$..secret_result")[0]
        conformance_result = jsonpath.jsonpath(res.json(), "$..conformance_result")[0]

        excel_analog.write(sheet_name, test_data['case_id'] + 1, 16,
                           str(secret_result['prv_match_app']))
        excel_analog.write(sheet_name, test_data['case_id'] + 1, 17,
                           str(secret_result['prv_match_function']))

if __name__ == '__main__':
    unittest.main()
