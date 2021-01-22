import unittest
import ddt
from common.excel_handler import excel_analog
from common.sheet_header import SheetHeader
from common.db_handler import DBHandler
import pymysql
import jsonpath
import json
import requests
from middleware.wf_login import LoginToken
login_token = LoginToken().login_token()
auth_token = LoginToken().auth_token(login_token)


sheet_name = 'detection_rate'
test_cases = excel_analog.read(sheet_name)
head_data = excel_analog.header(sheet_name)
#print(head_data)
header_data = SheetHeader(head_data)
#print(sheet_header)
print(header_data.__getattribute__('result'))


#通过task_id查询结果，并判断该检出的检出项是否检出
@ddt.ddt
class TestTaskResult(unittest.TestCase):
    @ddt.data(*test_cases)
    def test_task_results(self, test_case):
        task_id = test_case['task_id']
        case = test_case['case']
        row = test_case['case_id'] + 1
        url = "http://workflow-cp-fe.prod.k8ss.cc/v1/graph"
        request_body = {"operationName": "task", "variables": {"taskId": task_id},
                        "query": "query task($taskId: String!) {  task(taskId: $taskId) "
                                 "{    app    completedAt   createdAt    expiredAt    priority    taskId    status    outputs    updatedAt    workflow  }}"
                        }
        headers = {'Authorization': 'bearer {}'.format(auth_token), 'Content-Type': 'application/json'}
        print(headers)
        res = requests.post(url=url, json=request_body, headers=headers)
        print(request_body)
        print(res.json())
        res1 = jsonpath.jsonpath(res.json(), "$.data.task.outputs")
        print(res1)
        outputs = json.loads(res1[0])
        # sql = "select outputs from `hw-a-workflow-test2`.tasks where task_id='{}'".format(task_id)
        # cur = DBHandler()
        # res = cur.get_one(sql=sql)
        # result = json.loads(res[0])
        # print(result,type(result))
        #
        # print(sql)
        # res = cur.get_one(sql)
        # outputs = json.loads(res[0])
        print("#############################这是写的第{}条数据".format(row))
        # print("############查到的结果为{}".format(outputs))

        downloader_errcode = jsonpath.jsonpath(outputs, '$.downloader.err_code')
        if downloader_errcode != False:
            excel_analog.write(sheet_name=sheet_name, row=row, column=header_data.__getattribute__('downloader'),
                             data=downloader_errcode[0])
        else:
            excel_analog.write(sheet_name=sheet_name, row=row, column=header_data.__getattribute__('downloader'),
                             data="未找到errcode，下载失败")

        stage2_errmsg = jsonpath.jsonpath(outputs, '$.analogstage2.err_msg')
        stage2_errcode = jsonpath.jsonpath(outputs, '$.analogstage2.err_code')
        print(stage2_errcode,stage2_errmsg,type(stage2_errcode[0]))
        print(stage2_errcode != False)
        print(stage2_errcode[0] == 1120000)
        if stage2_errcode != False:
            assert_result = 'fail'
            try:
                self.assertEqual(stage2_errcode[0], 1120000)
                stage2_info = jsonpath.jsonpath(outputs, '$.analogstage2.data.info')
                if stage2_info != False:
                    stage2_result = stage2_info[0]
                    for i in stage2_result:
                        if i['type'] == case:
                            real_case_result = i['state']

                            try:
                                self.assertEqual(True, real_case_result)
                                assert_result = 'success'
                            except Exception as e:
                                print(e)
                                assert_result = 'fail'
                                raise e
                            finally:
                                excel_analog.write(sheet_name, row, column=header_data.__getattribute__('case_result'),
                                                   data="{}-{}".format(i['state'], i["data"]))

            except Exception as e:
                print(e)
                assert_result = 'fail'
                raise e
            finally:
                excel_analog.write(sheet_name, row, column=header_data.__getattribute__('result'),
                                   data=assert_result)
                excel_analog.write(sheet_name=sheet_name, row=row, column=header_data.__getattribute__('analogstage2'),
                                   data=stage2_errmsg[0])

        else:
            excel_analog.write(sheet_name=sheet_name, row=row, column=header_data.__getattribute__('analogstage2'),
                                 data="未找到errmsg，二阶段超时未回调或未进行")




if __name__ == '__main__':
    unittest.main()
