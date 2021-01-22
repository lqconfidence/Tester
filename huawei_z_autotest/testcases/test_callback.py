#回调，已经写完了
import unittest
from common.request_handler import Http
import requests
from common.excel_handler import excel_callback_public
from common.loger_handler import mylog
from libs.ddt import ddt,data
from common.yaml_handler import myconf
from common.pubic_testdata_handler import HandlerPublicTestData
from common.db_handler import DBHandler
from common.sheet_header import SheetHeader
import time
import jsonpath
import json

sheet_name = 'callback-v3'
head_data = excel_callback_public.header(sheet_name)
#print(head_data)
sheet_header = SheetHeader(head_data)

@ddt
class TestCallback(unittest.TestCase):
    testdatas = excel_callback_public.read(sheet_name)
    hpt = HandlerPublicTestData()
    task_id_sql = "select task_id from `public_api_test`.tasks where task_id = '010b06b4-b329-4250-b672-c95a7d27daa7'"
    result_sql = "select result from `public_api_test`.tasks where task_id = '010b06b4-b329-4250-b672-c95a7d27daa7'"
    secret_result_sql = "select result from `public_api_test`.tasks where task_id = 'ba8268d1-aebc-4cc3-bd5d-521f6e6697db' and type = 'secret'"
    conformance_result_sql = "select result from `public_api_test`.tasks where task_id = 'ba8268d1-aebc-4cc3-bd5d-521f6e6697db' and type = 'conformance'"

    db = DBHandler()
    @data(*testdatas)
    def test_callback(self, test_data):
        #准备测试数据，将excel中解析出来的字段保留
        url = "http://irregular-app-detect-callback.d.k8ss.cc/v3/autocb"
        testdata = test_data['json']
        case_id = test_data['case_id']
        row = case_id + 1
        case = test_data['case']
        detect_type = test_data['type']
        #request_body = self.hpt.handler_test_data(data=testdata, sql=self.task_id_sql, before_str="#req_id#")

        req_id = 'ba8268d1-aebc-4cc3-bd5d-521f6e6697db'
        request_body = testdata.replace("#req_id#", req_id)
        request_body = json.loads(request_body)
        headers1 = {'Content-Type': 'application/json'}
        print("callback的请求参数是")
        print(request_body,type(request_body))
        #发送callback/v3接口请求，发完等待1秒，确保public-api已更新

        res =requests.post(url=url,json=request_body,headers=headers1)
        print('回调的响应是？')
        print(res.json())
        time.sleep(5)
        ###下面是请求外网接口(public-api)######
        task_result = ""
        pa_body = {"request": [{"task_id": req_id, "type": ["secret","conformance"]}]}
        #请求PA的status接口，查询结果
        pa_url = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/status?tpl=hw-z-p'
        headers = {'X-HOST': 'public-api.d.k8ss.cc', 'X-PORT': '80', 'X-SK': 'testtest',
                   'Content-Type': 'application/json'}
        pa_res = requests.post(url=pa_url, data=None, json=pa_body, cookies=None, headers=headers)
        expected = test_data['expected']
        print(pa_res.json())
        data = pa_res.json()['data'][0]
        print(data, type(data))
        print(case)
        if 'err_code' in case:
            actual = data[detect_type][case]
        else:
            actual = jsonpath.jsonpath(data, '$..{}'.format(case))[0]
        print("预期结果是{}，实际结果是{}".format(expected,actual))
        assert_result = ""
        try:
            self.assertIn(str(expected),str(actual))
            assert_result = "success"
            excel_callback_public.write(sheet_name, row, column=sheet_header.__getattribute__('actual_case_result'),
                                        data=str(actual))

        except Exception as e:
            assert_result = 'fail'
            excel_callback_public.write(sheet_name, row, column=sheet_header.__getattribute__('actual_case_result'),
                                        data=str(actual))
            raise e
        finally:

            excel_callback_public.write(sheet_name, row, column=sheet_header.__getattribute__('assert_result'),
                                        data=assert_result)
            time.sleep(3)





if __name__ == '__main__':
    unittest.main()
