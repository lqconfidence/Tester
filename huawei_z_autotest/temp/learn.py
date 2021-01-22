from threading import Thread

import requests

import unittest
import ddt
from common.loger_handler import mylog
import json
import requests
import time
import jsonpath
from temp.task_id import TaskId
res_list = []
dict_res = {"task_id":"", "result":""}


from common.excel_handler import excel_callback_public

sheet_name = 'hwz_inspection'

test_datas = excel_callback_public.read(sheet_name)
print(test_datas)
class MyThread(Thread):  #
    def run(self):
        print("进入线程")
        get_result(res_list)


def get_result(res_list):
    print("进入获取结果函数{}".format(res_list))
    for i in res_list:
        request_body = {"request": [{"task_id": i['task_id'], "type": ["secret", "conformance"]}]}
        url = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/status?tpl=hw-z-p'
        headers = {'X-HOST': 'public-api.d.k8ss.cc', 'X-PORT': '80', 'X-SK': 'testtest',
                   'Content-Type': 'application/json'}
        prv_start_policy = False
        j = 0
        while prv_start_policy == False:
            res = requests.post(url=url, data=None, json=request_body, cookies=None, headers=headers)
            j += 1
            print("这是第{}次请求".format(j))
        i['result'] = res.json()


for test_data in test_datas:
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
        res = requests.post(url=url, data=None, json=request_body, cookies=None, headers=headers)
        task_id = jsonpath.jsonpath(res.json(),"$..task_id")[0]
        excel_callback_public.write(sheet_name, test_data['case_id'] + 1, 8, str(task_id))
        dict_res['task_id'] = task_id
        res_list.append(dict_res)
        print("投放任务是{}".format(test_data['case_id'] + 1), "这时候的res_list是{}".format(res_list))
        t1 = MyThread()
        t1.run()


#for i in range(100):
#     id = requests.get('获取id')
#     '''id存进表格'''
#     '''开启一个线程'''
#     t1=MyThread()
#     t1.start()
#     '''循环读取表格得到一个列表嵌套字典'''
#     '''遍历列表，判断每个字典的结果列是否为空并且flag是否为1，不为且不为1时进行解析'''
#     '''解析'''
#     '''在表格写一列flag,解析完的flag为1'''

