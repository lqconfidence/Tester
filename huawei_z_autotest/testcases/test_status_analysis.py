# -*-coding:utf-8 -*-
# @Time:2020/5/11 11:25
# @Author:a'nan
# @Email:934257271
# @File:test-hwa-public-inspection.py
######public-api，hw-z-p渠道投放任务。
######
import unittest
import ddt
from common.loger_handler import mylog
import json
import requests
import time
import jsonpath

from common.excel_handler import excel_callback_public

sheet_name = 'hwz_inspection'

test_datas = excel_callback_public.read(sheet_name)
from common.sheet_header import SheetHeader
from testcases.test_hwz_public_inspection import TestPaInspection


head_data = excel_callback_public.header(sheet_name)
sheet_head = SheetHeader(head_data)


@ddt.ddt
class TestPaInspection(unittest.TestCase):

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    li_task_id = []

    @ddt.data(*test_datas)
    def test_inspection_pa(self, test_data):
        #ip = "http://irregular-app-detect-workflow.test.k8ss.cc"
        mylog.info('test data{}'.format(test_data))
        #url = ip + test_data['path']
        method = "POST"
        apk_url = test_data['apkurl']
        md5 = test_data['md5']
        privacyurl = test_data['privacyurl']
        apptype = test_data['apptype']
        introduction = test_data['introduction']
        flag = test_data['flag']
        #expected = test_data['expected']
        # 请求参数
        request_body = {	"request": [{		"md5": md5,		"url": apk_url,		"type": ["secret","conformance"],
                                                 "options": {
			"secret": {
				"apptype": apptype,
				"introduction": introduction,
				"flag": flag,
				"privacyurl": privacyurl
			}
		}
	}]
}
        res = None
        url = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/sample-inspection?tpl=hw-z-p'
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
                time.sleep(600)
        else:
            mylog.error('request method error')

        result = None

        task_id = jsonpath.jsonpath(res.json(),"$..task_id")[0]
        mylog.info('test result{}'.format(res.text))

        excel_callback_public.write(sheet_name, test_data['case_id'] + 1, 8, str(task_id))
        self.li_task_id.append(task_id)
        time.sleep(3)
    time.sleep(20)

    test_datas1 = excel_callback_public.read(sheet_name)
    print("查询结果前，表单数据为",test_datas1)
    @ddt.data(*test_datas1)
    def test_status_bev(self, test_data):
        #mylog.info('test data{}'.format(test_data))
        task_id = test_data['task_id']
        print("task_id ",task_id)
        print(test_data['case_id'] + 1)
        # 请求参数
        request_body = {    "request":[        {           "task_id":task_id,         "type": ["secret","conformance"]        }    ]}
        res = None
        url = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/status?tpl=hw-z-p'
        headers = {'X-HOST': 'public-api.d.k8ss.cc', 'X-PORT': '80', 'X-SK': 'testtest',
                   'Content-Type': 'application/json'}
        print("查询结果请求参数",request_body)
        secret_result = {}
        i = 1
        prv_start_policy = False
        while prv_start_policy == False:
            print("第{}次查询".format(i))
            res = requests.post(url=url, data=None, json=request_body, cookies=None, headers=headers)
            print(res.json())
            prv_start_policy = jsonpath.jsonpath(res.json(), "$..prv_start_policy")
            i+=1
            time.sleep(30)
        secret_result = jsonpath.jsonpath(res.json(), "$..secret_result")[0]
        conformance_result = jsonpath.jsonpath(res.json(), "$..conformance_result")[0]
        for i in secret_result.keys():
            print(i)
            excel_callback_public.write(sheet_name, test_data['case_id'] + 1, sheet_head.__getattribute__(i),
                                  str(jsonpath.jsonpath(secret_result, "$..{}".format(i))[0]))
        for i in conformance_result.keys():
            print(i)
            if i == 'err_code' or i == 'err_msg':
                continue
            excel_callback_public.write(sheet_name, test_data['case_id'] + 1, sheet_head.__getattribute__(i),
                                        str(jsonpath.jsonpath(conformance_result, "$..{}".format(i))[0]))

if __name__ == '__main__':
    unittest.main()

