# 调用爬虫接口进行爬虫
#
import unittest

import ddt
import requests
import json
import jsonpath

import time

#from common.db_handler import cursor
from common.excel_handler import excel_ppcrawler
from common.loger_handler import mylog
from common.setting import Config

test_data = excel_ppcrawler.read('ppcrawler_url')

@ddt.ddt
class TestPpcrawler(unittest.TestCase):

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_ppcrawler(self, test_data):
        url = "http://crawler.t.k8ss.cc/task/create"
        mylog.info('test data{}'.format(test_data))
        requestId = int(time.time())
        md5 = test_data['md5']
        method = "POST"
        privacy_url = test_data['privacy_url']
        # 请求参数
        request_body = {"urls": [privacy_url],  "requestId": str(requestId) }
        print(request_body,type(request_body))
        res = requests.post(url=url, json=request_body,  cookies=None)
        print(res.json())
        result = None
        errCode = jsonpath.jsonpath(res.json(),'$..errCode')[0]
        requestId = jsonpath.jsonpath(res.json(),'$..requestId')[0]
        title = jsonpath.jsonpath(res.json(),'$..title')[0]

        # text = jsonpath.jsonpath(res.json(), "$..text")
        # text1 = ''
        # if text == False:
        #     text1 = '没有找到text字段，爬虫失败了'
        # else:
        #     text1 = text[0]
        #
        # data = open(r"D:\AntiyData\{}.txt".format(md5),'w')
        # data.write(text1)
        if title == False:
            ti = "爬虫失败，没有获取到title"
        else:
            ti = title
        mylog.info('test result{}'.format(res.text))
        try:
            self.assertEqual(test_data['expected'],errCode)
            result = 'success'
        except Exception as e:
            mylog.error('assertion error,res is{}'.format(e))
            result = 'fail'
            raise e
        finally:
            #第7列写入task_id
            excel_ppcrawler.write('ppcrawler_url', test_data['case_id'] + 1, 7, result)
            excel_ppcrawler.write('ppcrawler_url', test_data['case_id'] + 1, 8, requestId)
            excel_ppcrawler.write('ppcrawler_url', test_data['case_id'] + 1, 9, ti)

        time.sleep(60)
