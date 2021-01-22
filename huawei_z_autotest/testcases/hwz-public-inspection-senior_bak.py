# -*-coding:utf-8 -*-
# @Time:2020/9/18 20:48
# @Author:a'nan
# @Email:934257271
# @File:hwz-public-inspection-senior.py

from common.excel_handler import excel_analog
import requests
import time
import jsonpath
import json
sheet_name = 'inspection'
test_datas = excel_analog.read(sheet_name)
print(test_datas[0], type(test_datas))
url = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/sample-inspection?tpl=hw-z-p'
headers = {'X-HOST': 'public-api.d.k8ss.cc', 'X-SK': 'testtest',
                   'Content-Type': 'application/json'}

step = 2
sleep_time = 900


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
for i in range(0, mod * step, step):
    for j in range(i, i + step):
        case_id = test_datas[j]['case_id']
        print("case_id为{}".format(case_id))
        row = case_id + 1
        apk_url = test_datas[j]['apkurl']
        md5 = test_datas[j]['md5']
        apptype = str(test_datas[j]['apptype'])
        introduction = str(test_datas[j]['introduction'])
        flag = str(test_datas[j]['flag'])
        privacyurl = str(test_datas[j]['privacyurl'])
        if "None" in apptype:
            apptype = apptype.replace('None', '')
        if "None" in introduction:
            introduction = introduction.replace('None', '')
        if "None" in flag:
            flag = flag.replace('None', '')
        if "None" in privacyurl:
            privacyurl = privacyurl.replace('None', '')
        request_body = {"request": [{	"md5": md5,		"url": apk_url,		"type": ["secret" ,"conformance"],
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
        #print("当前请求参数为的值为###########{}\n ".format(request_body), type(request_body))
        try:
            res = requests.post(url=url, json=request_body,headers=headers)
            print("请求响应为{}".format(res.json()))
            task_id = jsonpath.jsonpath(res.json(), "$..task_id")[0]
            excel_analog.write(sheet_name=sheet_name, row=row, column=8, data=task_id)
        except Exception as e:
            print('request -post error the reason is {}'.format(e))
            raise e
    time.sleep(sleep_time)
for i in range(-rem, 0, 1):
    print(test_datas[i], type(test_datas[i]))
    case_id = test_datas[i]['case_id']
    print("case_id为{}".format(case_id))
    row = case_id + 1
    apk_url = test_datas[i]['apkurl']
    md5 = test_datas[i]['md5']
    apptype = str(test_datas[i]['apptype'])
    introduction = str(test_datas[i]['introduction'])
    flag = str(test_datas[i]['flag'])
    privacyurl = str(test_datas[i]['privacyurl'])
    if "None" in apptype:
        apptype = apptype.replace('None', '')
    if "None" in introduction:
        introduction = introduction.replace('None', '')
    if "None" in flag:
        flag = flag.replace('None', '')
    if "None" in privacyurl:
        privacyurl = privacyurl.replace('None', '')
    request_body = {"request": [{"md5": md5, "url": apk_url, "type": ["secret", "conformance"],
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
    #print("当前请求参数为的值为###########{}\n ".format(request_body),type(request_body))
    #request_body = json.loads(request_body)
    try:
        res = requests.post(url=url, json=request_body, headers=headers)
        print("请求响应为{}".format(res.json()))
        task_id = jsonpath.jsonpath(res.json(), "$..task_id")[0]
        excel_analog.write(sheet_name=sheet_name, row=row, column=8, data=task_id)
    except Exception as e:
        print('request -post error the reason is {}'.format(e))
        raise e

