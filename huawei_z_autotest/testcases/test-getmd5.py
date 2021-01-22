######
###下载 得到MD5，并将MD5 写入excel，方便外网投放
import unittest

import ddt
import requests
import jsonpath
import json

import time
from common.excel_handler import excel_static_privacy
from common.loger_handler import mylog


test_data = excel_static_privacy.read('url-md5')

@ddt.ddt
class TestInnerIssueAPI(unittest.TestCase):

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_inspection_md5(self, test_data):
        ip = "http://irregular-app-detect-workflow.test.k8ss.cc"
        mylog.info('test data{}'.format(test_data))
        url = ip + test_data['path']
        method = test_data['method']
        task_id = test_data['task_id']
        apk_url = test_data['apk_url']
        # 请求参数
        request_body = {"query":"query task($taskId: String!)\n{  task(taskId: $taskId) \n  {   \n  app\n  completedAt  \n  createdAt    \n  expiredAt   \n  priority     \n  taskId   \n \n  outputs \n  updatedAt   \n  }\n}","variables":{"taskId":task_id},"operationName":"task"}
        headers = {'Authorization':'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkc3AiOiIlRTYlQUMlQTclRTklOTglQjMlRTklOTQlOTAiLCJlbWwiOiJvd'
                                   'XlhbmdydWlAYW50aXkuY24iLCJleHAiOjE1ODkxODk4MjMsIm5iZiI6MTU4OTE2NzkyMywidWlkIjoib3V5YW5ncnVpMSJ9.Iob_T5HrPX0UHvK0JK9K_tUEr3V5Fskcys5sSJO7u-s'}
        res = None

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
            except Exception as e:
                mylog.error('request -post error the reason is {}'.format(e))
        else:
            mylog.error('request method error')

        #用例执行结果
        result = None
        #解析outputs
        outputs = jsonpath.jsonpath(res.json(), '$..outputs')
        print(*outputs, type(*outputs))
        outputs_json = json.loads(*outputs)
        md5 = jsonpath.jsonpath(outputs_json, '$..md5')[0]
        info = jsonpath.jsonpath(outputs_json, '$..info')
        staticprivacy = jsonpath.jsonpath(outputs_json, '$..staticprivacy')
        print(info, type(info))

        mylog.info('test result{}'.format(res.text))
        try:
            self.assertEqual(200, res.status_code)
            result = 'success'
        except Exception as e:
            mylog.error('assertion error,res is{}'.format(e))
            result = 'fail'
            raise e
        finally:
            #第6列写入MD5，来自download；
            if result == 'success':
                if md5 == False:
                    excel_static_privacy.write('url-md5', test_data['case_id'] + 1, 7, "下载异常")
                elif md5 != False:
                    excel_static_privacy.write('url-md5', test_data['case_id'] + 1, 7, "{}".format(md5))










