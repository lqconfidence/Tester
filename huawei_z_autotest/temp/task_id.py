# -*-coding:utf-8 -*-
# @Time:2020/10/27 18:32
# @Author:a'nan
# @Email:934257271
# @File:task_id.py
import requests
import jsonpath
import time

from common.excel_handler import excel_callback_public

sheet_name = 'hwz_inspection'

test_datas = excel_callback_public.read(sheet_name)
from common.sheet_header import SheetHeader


head_data = excel_callback_public.header(sheet_name)
sheet_head = SheetHeader(head_data)

class  TaskId():
    task_id = []
    def task_id_append(self, task_id):
        self.task_id.append(task_id)

    def task_id_result(self,task_id_li):

        li_res = []
        for task_id in task_id_li:
            dict_res = {}
            request_body = {"request": [{"task_id": task_id, "type": ["secret", "conformance"]}]}
            res = None
            url = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/status?tpl=hw-z-p'
            headers = {'X-HOST': 'public-api.d.k8ss.cc', 'X-PORT': '80', 'X-SK': 'testtest',
                       'Content-Type': 'application/json'}
            print("查询结果请求参数", request_body)
            secret_result = {}
            i = 1
            prv_start_policy = False
            while prv_start_policy == False:
                print("第{}次查询".format(i))
                res = requests.post(url=url, data=None, json=request_body, cookies=None, headers=headers)
                print(res.json())
                prv_start_policy = jsonpath.jsonpath(res.json(), "$..prv_start_policy")
                i += 1
            # secret_result = jsonpath.jsonpath(res.json(), "$..secret_result")[0]
            # conformance_result = jsonpath.jsonpath(res.json(), "$..conformance_result")[0]
            dict_res[task_id] = res.json()
        li_res.append(dict_res)
        return li_res

    def list_to_excel(self, li_res):
        for test_data in test_datas:
            for i in li_res:
                if test_data['task_id'] in str(i):
                    secret_result = jsonpath.jsonpath(i, "$..secret_result")[0]
                    conformance_result = jsonpath.jsonpath(i, "$..conformance_result")[0]
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



if __name__ =="__main__":
    test = TaskId()
    test.task_id = ['293099e7-7903-48b6-a189-1651ea71cffa','0ac1c453-ace2-4dc4-afa1-d84257e6fa0e','64daf006-0bd5-44a0-96af-141009395d4f']
    li_res = test.task_id_result(test.task_id)
    print(li_res)
    test.list_to_excel(li_res)
