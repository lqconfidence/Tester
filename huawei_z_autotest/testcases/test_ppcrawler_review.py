#由任务调度配置  直接进行语义分析。还没写完

import unittest
import ddt
import requests
import json

import time
import jsonpath

from common.db_handler import DBHandler
from common.excel_handler import excel
from common.excel_handler import excel_static_privacy
from common.loger_handler import mylog
from common.setting import Config


test_data = excel_static_privacy.read('inspection_url')

@ddt.ddt
class TestStaticPrivacy(unittest.TestCase):

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_ppcrawler_review(self, test_data):
        ip = "http://irregular-app-detect-workflow.test.k8ss.cc"
        mylog.info('test data{}'.format(test_data))
        url = ip + test_data['path']
        method = "POST"
        apk_url = test_data['apkurl']
        privacyUrl = test_data['privacyUrl']
        # 请求参数
        request_body = {"app_id": "crawler-privacyreview",
                         "apkUrl": "{}".format(apk_url),
                        "privaryUrl":"{}".format(privacyUrl),
                         "priority": 1}

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
                res = requests.post(url=url, data=None, json=request_body, cookies=None)
            except Exception as e:
                mylog.error('request -post error the reason is {}'.format(e))
        else:
            mylog.error('request method error')

        result = None

        mylog.info('test result{}'.format(res.text))
        try:
            self.assertEqual(test_data['expected'], res.json()['err_code'])
            result = 'success'
        except Exception as e:
            mylog.error('assertion error,res is{}'.format(e))
            result = 'fail'
            raise e
        finally:
            #第7列写入task_id
            excel_static_privacy.write('inspection_url', test_data['case_id'] + 1, 9, jsonpath.jsonpath(res.json(),"$..createTask"))
            excel_static_privacy.write('inspection_url', test_data['case_id'] + 1, 8, result)

