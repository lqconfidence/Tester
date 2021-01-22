# -*-coding:utf-8 -*-
# @Time:2020/5/8 14:38
# @Author:a'nan
# @Email:934257271
# @File:test_static_privacy.py
###静态隐私提取的结果分析，已写完
import unittest

import ddt
import requests
import jsonpath
import json

import time
from common.excel_handler import excel_static_privacy
from common.loger_handler import mylog


test_data = excel_static_privacy.read('static_privacy_res')

@ddt.ddt
class TestInnerIssueAPI(unittest.TestCase):

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_inspection_staprv(self, test_data):
        ip = "http://irregular-app-detect-workflow.test.k8ss.cc"
        mylog.info('test data{}'.format(test_data))
        url = ip + test_data['path']
        method = test_data['method']
        task_id = test_data['task_id']
        apk_url = test_data['apk_url']
        # 请求参数
        request_body = {"query":"query task($taskId: String!)\n{  task(taskId: $taskId) \n  {   \n  app\n  completedAt  \n  createdAt    \n  expiredAt   \n  priority     \n  taskId   \n \n  outputs \n  updatedAt   \n  }\n}","variables":{"taskId":task_id},"operationName":"task"}
        headers = {'Authorization':'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkc3AiOiIlRTYlQUMlQTclRTklOTglQjMlRTklOTQlOTAiLCJlbWwiOiJvdXlhbmdydWlAYW50aXkuY24iLCJleHAiOjE1OTAwNDQzODUsIm5iZiI6MTU5MDAyMjQ4NSwidWlkIjoib3V5YW5ncnVpMSJ9.'
                                   'L0CGmbXTSnSGqgSgHmJIoZ-HJ32TjAALHtFTu3CZdBQ'}
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
            #第7列写入完整static_privacy_result，第8列写入global_broadcast，第九列写入lock_screen_ad
            #第10列mulite_icon；第十一列privacy_text，第十二列suspected_privacy_activity，十三列other_activity
            #第14列，写入result
            #excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 7, str(res.json()['data']['tasks'][0]))
            #excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 8, result)
            excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 14, result)
            if result == 'success':
                if md5 == False:
                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 6, "下载异常")
                elif md5 != False:
                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 6, "{}".format(md5))
                if info == False:
                    if staticprivacy == False:
                        excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 7,
                                              "静态隐私提取失败-没有staticprivacy结果")
                    else:
                        excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 7,
                                              "静态隐私提取失败-{}".format(staticprivacy))

                else:
                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 7,
                                          "{}".format(info))
                    for i in info:
                        print("info里面的元素及类型",i,type(i))
                        for j in i:
                            print("info里面的里面的元素及类型",j,type(j))
                            if j['type'] == 'global_broadcast':
                                if j['state'] == False:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 8,
                                                          "global_broadcast检出为{}，data为{}".format(j['state'],j['data']))
                                else:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 8,
                                                          "global_broadcast检出为{}，data为{}".format(j['state'], j['data']))
                            if j['type'] == 'lock_screen_ad':
                                if j['state'] == False:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 9,
                                                          "lock_screen_ad检出为{}，data为{}".format(j['state'],j['data']))
                                else:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 9,
                                                          "lock_screen_ad检出为{}，data为{}".format(j['state'], j['data']))
                            if j['type'] == 'mulite_icon':
                                if j['state'] == False:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 10,
                                                          "mulite_icon检出为{}，data为{}".format(j['state'],j['data']))
                                else:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 10,
                                                          "mulite_icon检出为{}，data为{}".format(j['state'], j['data']))
                            if j['type'] == 'privacy_text':
                                if j['state'] == False:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 11,
                                                          "privacy_text检出为{}，data为{}".format(j['state'],j['data']))
                                else:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 11,
                                                          "privacy_text检出为{}".format(j['state']))
                            if j['type'] == 'suspected_privacy_activity':
                                if j['state'] == False:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 12,
                                                          "suspected_privacy_activity检出为{}，data为{}".format(j['state'],j['data']))
                                else:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 12,
                                                          "suspected_privacy_activity检出为{}，data为{}".format(j['state'], j['data']))

                            if j['type'] == 'other_activity':
                                if j['state'] == False:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 13,
                                                          "other_activity检出为{}，data为{}".format(j['state'], j['data']))
                                else:
                                    excel_static_privacy.write('static_privacy_res', test_data['case_id'] + 1, 13,
                                                          "other_activity检出为{}，data为{}".format(j['state'], j['data']))










