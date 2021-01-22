# -*-coding:utf-8 -*-
# @Time:2020/8/31 15:53
# @Author:a'nan
# @Email:934257271
# @File:hwz_wf_inspection_senior.py

from common.excel_handler import excel_aosp
import requests
import time
import jsonpath

sheet_name = 'test'
test_datas = excel_aosp.read(sheet_name)

"""
#####只需要修改以下三个字段的值。下面的配置表示：向内网hw-z-only-analog-copy渠道投放任务，每隔十五分钟投5个任务######
#!!!!!!!如果不知道使用哪个渠道，请来咨询我！
"""
#内网渠道
app_id = 'hw-z-only-analog-copy'
#每次投放任务数量，比如每次投3个
step = 3
#投放等待时间，比如，每15分钟投一次.下面时间为秒，请用分钟*60。
sleep_time = 900


url = 'http://irregular-app-detect-workflow.test.k8ss.cc/v2/task/sample-inspection'


def mod(a, step):
    c = a / step
    r = int(c)
    return r


def rem(a, step):
    c = int(a / step)
    r = a - c * step
    return r



len = test_datas.__len__()

mod = mod(len, step)
rem = rem(len, step)
print("数组长度为{}".format(len),"余数为{}".format(rem))
if mod == 0:
    for i in range(0, len, step):
        for j in range(i, i + step):
            case_id = test_datas[j]['case_id']
            print("case_id为{}".format(case_id))
            row = case_id + 1
            apk_url = test_datas[j]['apk_url']
            md5 = test_datas[j]['md5']
            request_body = {
                "task_id": "d8709db0-41e3-462e-a6aa-111111111111",
                "app_id": app_id,
                "priority": 1,
                "options": {
                    "apkUrl": apk_url,
                    "md5": md5
                }
            }
            print("当前请求参数为的值为###########{}\n".format(request_body))
            try:
                res = requests.post(url=url, json=request_body)
                print("请求响应为{}".format(res.json()))
                excel_aosp.write(sheet_name=sheet_name, row=row, column=9, data=str(res.json()))
                task_id = jsonpath.jsonpath(res.json(), '$..task')[0]
                excel_aosp.write(sheet_name=sheet_name, row=row, column=8, data=task_id)
            except Exception as e:
                raise e

        time.sleep(sleep_time)

else:
    for i in range(0, mod * step, step):
        print("i的值为{}".format(i))
        li = []
        for j in range(i, i + step):
            print(test_datas[j], type(test_datas[j]))
            case_id = test_datas[j]['case_id']
            print("case_id为{}".format(case_id))
            row = case_id + 1
            apk_url = test_datas[j]['apk_url']
            md5 = test_datas[j]['md5']
            request_body = {
                "task_id": "d8709db0-41e3-462e-a6aa-111111111111",
                "app_id": app_id,
                "priority": 1,
                "options": {
                    "apkUrl": apk_url,
                    "md5": md5
                }
            }
            print("当前请求参数为的值为###########{}\n".format(request_body))
            try:
                res = requests.post(url=url, json=request_body)
                print("请求响应为{}".format(res.json()))
                excel_aosp.write(sheet_name=sheet_name, row=row, column=9, data=str(res.json()))
                task_id = jsonpath.jsonpath(res.json(), '$..task')[0]
                excel_aosp.write(sheet_name=sheet_name, row=row, column=8, data=task_id)
            except Exception as e:
                raise e
        time.sleep(sleep_time)

    for i in range(-rem, 0, 1):
        print(test_datas[j], type(test_datas[j]))
        case_id = test_datas[j]['case_id']
        print("case_id为{}".format(case_id))
        row = case_id + 1
        apk_url = test_datas[j]['apk_url']
        md5 = test_datas[j]['md5']
        request_body = {
            "task_id": "d8709db0-41e3-462e-a6aa-111111111111",
            "app_id": app_id,
            "priority": 1,
            "options": {
                "apkUrl": apk_url,
                "md5": md5
            }
        }
        print("当前请求参数为的值为###########{}\n ".format(request_body))
        try:
            res = requests.post(url=url, json=request_body)
            print("请求响应为{}".format(res.json()))
            excel_aosp.write(sheet_name=sheet_name, row=row, column=9, data=str(res.json()))
            task_id = jsonpath.jsonpath(res.json(), '$..task')[0]
            excel_aosp.write(sheet_name=sheet_name, row=row, column=8, data=task_id)
        except Exception as e:
            raise e

