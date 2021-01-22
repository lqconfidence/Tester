import unittest
import ddt
from common.excel_handler import excel_callback_public
from common.sheet_header import SheetHeader
import requests
import pymysql
import json
import jsonpath

sheet_name = 'hwz_inspection'
test_cases = excel_callback_public.read(sheet_name)
head_data = excel_callback_public.header(sheet_name)
#print(head_data)
sheet_header = SheetHeader(head_data)
#print(sheet_header)
#print(sheet_header.__getattribute__('result'))


#通过task_id查询结果，并判断该检出的检出项是否检出
@ddt.ddt
class TestTaskResult(unittest.TestCase):
    @ddt.data(*test_cases)
    def test_task_results(self, test_case):
        apk_url = test_case['apkurl']
        md5 = test_case['md5']
        expected_case_result = test_case['expected_case_result']
        case = test_case['case']
        task_id = test_case['task_id']
        row = test_case['case_id'] + 1
        # 请求参数
        request_body = {"request": [		{"task_id": task_id,				"type": ["secret","conformance"]}		]}

        res = None
        url = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/status?tpl=hw-z-p'
        headers = {'X-HOST': 'public-api.d.k8ss.cc', 'X-PORT': '80', 'X-SK': 'testtest',
                   'Content-Type': 'application/json'}
        result = requests.post(url=url, data=None, json=request_body, cookies=None, headers=headers).json()
        print(request_body)
        # print(result,type(result))
        # compliance = result['data'][0]
        # print("compliance"+str(compliance))
        real_case_result = jsonpath.jsonpath(result,"$..{}".format(case))[0]
        real_case_result_state = jsonpath.jsonpath(result, "$..{}".format(case))[0]['state']
        print(real_case_result)
        assert_result = 'fail'
        try:
            print("预期结果是{}，实际结果是{}".format(expected_case_result,real_case_result_state))
            self.assertEqual(expected_case_result, str(real_case_result_state))
            assert_result = 'success'
        except Exception as e:
            print(e)
            assert_result = 'fail'
            raise e
        finally:
            excel_callback_public.write(sheet_name, row, column=sheet_header.__getattribute__('real_case_result'), data=str(real_case_result))
            excel_callback_public.write(sheet_name, row, column=sheet_header.__getattribute__('assert_result'), data=assert_result)



if __name__ == '__main__':
    unittest.main()

