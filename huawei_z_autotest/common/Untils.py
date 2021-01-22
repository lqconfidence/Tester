#！/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__  = antiy

from common.handle_ini import HandInit,Myparse
from common.handle_xlsx import HandleXlsx
import requests
import time
import jsonpath
import json


def put_rate(case_id,step,interval_time):
    if not (int(case_id) % step) and case_id != None:
        time.sleep(interval_time)

def post_hw_task(request_body):
    url1 = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/sample-inspection?tpl=hw-z-p'
    headers1 = {'X-HOST': 'public-api.d.k8ss.cc', 'X-SK': 'testtest',
                     'Content-Type': 'application/json'}
    response1 = requests.post(url=url1, json=request_body, headers=headers1)
    print(response1.text + time.ctime())
    res = json.loads(response1.text)
    task_id = res['data']['tasks'][0]['task_id']
    return task_id

def get_hw_result(task_id,rownum):

    handle_excel1 = HandleXlsx("callback_public.xlsx")
    url2 = 'http://utils-signature-proxy.d.k8ss.cc/v1/task/status?tpl=hw-z-p'
    headers2 = {'X-HOST': 'public-api.d.k8ss.cc', 'X-PORT': '80', 'X-SK': 'testtest',
                     'Content-Type': 'application/json'}
    request_body2 = {"request": [{"task_id": task_id, "type": ["secret", "conformance"]}]}
    handle_excel1.excel_write_data(rownum, 8, task_id)
    while True:
        res = requests.get(url=url2, json=request_body2, headers=headers2)
        if str(jsonpath.jsonpath(res.json(), "$..conformance_result")) != "[{}]":  #测试时取反
            time.sleep(5)
            result_str = json.dumps(res.text)
            handle_excel1.excel_write_data(rownum, 13, result_str)
            break
    print(res.json())

def calculateCheckoutRate():

    h = HandInit("CheckingRateConfig.ini")
    myparse = Myparse()
    myparse.read(h.file_path, encoding="utf-8")
    except_reulst=myparse.parse_dict()

    handle_excel = HandleXlsx("callback_public.xlsx")
    real_case_result=handle_excel.get_columns_values('M')
    rows=handle_excel.get_rows()
    rows=rows - 1
    reslut_ck = {}

    for key1, value1 in except_reulst.items():
        for key2, value2 in value1.items():
            reslut_ck[key2]=0
            n = 1
            for i in real_case_result:
                n += 1
                if i!= None:
                    data1 = json.loads(i)
                    print(data1)
                    print("$..{}.{}.state".format(key1,key2))
                    res_data=jsonpath.jsonpath(data1,"$..{}.{}.state".format(key1,key2))
                    print("res_date is {}".format(res_data))
                    if res_data:
                        if res_data[0] == value2:
                            reslut_ck[key2] += 1
                        else:
                            handle_excel.excel_write_data(n, 14, "Fail")#有一个错误就判定失败
                            print("res_data[0] is {},value2 is {}".format(res_data[0],value2))

    print("检出：{}".format(reslut_ck))
    m=1
    for k in reslut_ck:
        m+= 1
        strs="total:{}，{}检出数为{}，检出率:{}%,Time:{}".format(rows,k,reslut_ck[k],(reslut_ck[k]/rows),time.ctime())
        print(strs)
    return reslut_ck

def calculateCaptureRate():

    h = HandInit("CaptureLostRate.ini")
    myparse = Myparse()
    myparse.read(h.file_path, encoding="utf-8")
    except_reulst = myparse.parse_dict()
    print(except_reulst)

    handle_excel = HandleXlsx("callback_public.xlsx")
    real_case_result = handle_excel.get_columns_values('M')
    rows = handle_excel.get_rows()
    rows = rows - 1
    effective_num = 0
    reslut_ck = {}
    for key1, value1 in except_reulst.items():
        for key2, value2 in value1.items():
            if value2 == 'True':
                effective_num += 1
                reslut_ck[key2] = 0
                for i in real_case_result:
                    if i != None:
                        data1 = json.loads(i)
                        print(data1)
                        print("$..{key1}.{key2}.data[0].bitmap_path".format(key1=key1,key2=key2))
                        res_data1 = jsonpath.jsonpath(data1,"$..{key1}".format(key1=key1,key2=key2))
                        res_data2 = jsonpath.jsonpath(data1,"$..{key1}.{key2}.data".format(key1=key1,key2=key2))
                        res_data = jsonpath.jsonpath(data1,"$..{key1}.{key2}.data[0].bitmap_path".format(key1=key1,key2=key2))
                        print("res_date is {}".format(res_data))

                        if not res_data or res_data1 == False or res_data2 == False:
                            reslut_ck[key2] += 1
                        else:
                            print("res_data[0] is {}".format(res_data[0]))
                            print("value2 is {}".format(value2))

    print("截图缺失：{}".format(reslut_ck))
    n=1
    for k in reslut_ck:
        n += 1
        strs="total,{};需截图:{}，{}无截图数:{},截图缺失率:{}%,Time:{}".format(rows,effective_num,k,reslut_ck[k],(reslut_ck[k]/rows),time.ctime())
        print(strs)

    return reslut_ck

def parse_json(check_reslut,capture_result):

    try:
        handle_excel = HandleXlsx("callback_public.xlsx")
        real_case_result = handle_excel.get_columns_values('M')
        row_v = 1
        for d in real_case_result:

            row_v += 1

            res1=jsonpath.jsonpath(eval(json.loads(d)),"$..secret_result")
            print("res1 获取 secret_result的值为： {}".format(res1))

            res2=jsonpath.jsonpath(eval(json.loads(d)),"$..conformance_result")
            print("res2 获取 conformance_result的值为 ：{}".format(res2))

            res=dict(res1[0],**res2[0])

            n = 1
            for key,value in res.items():
                n += 1
                handle_excel.excel_write_data(1, 17 + n, key)
                handle_excel.excel_write_data(row_v, 17 + n, str(value))

        coulmns=handle_excel.get_rows_values(1)
        for col in coulmns:
            for key1,value1 in check_reslut.items():
                if key1 == col:
                    handle_excel.excel_write_data(row_v + 1,coulmns.index(col) + 1,"total:{row_v}，{col}检出数为{value1}，检出率:{checkout}%".format(row_v=row_v-1,col=col,value1=value1,checkout=(value1/row_v-1)))

        for col in coulmns:
            for key1,value1 in capture_result.items():
                if key1 == col:
                    handle_excel.excel_write_data(row_v + 2,coulmns.index(col) + 1,"total,{row_v},{col}无截图数:{value1},截图缺失率:{capturelost}%".format(row_v=row_v-1,col=col,value1=value1,capturelost=(value1/row_v-1)))

    except:
        print("json parsed error!!!!!!!!!!")



if __name__=="__main__":
    res1= calculateCheckoutRate()
    res2= calculateCaptureRate()
    # captureLost={'bev_illegal_content': 0, 'bev_fake_alert': 0, 'bev_keep_alive': 0, 'bev_disturb': 0, 'bev_force': 0, 'bev_hinder_app': 0, 'bev_enable_debug': 0, 'bev_display_bkg': 0, 'bev_resident_notification': 0, 'bev_outside_ad': 0, 'bev_hard_uninstall': 0, 'prv_start_policy': 0, 'prv_refuse_authorize': 0, 'prv_apply_repeat': 0, 'prv_default_app': 0, 'prv_apply_onetime': 0, 'prv_policy_delay': 0}
    # checkouts={'bev_illegal_content': 9, 'bev_bundle_download': 9, 'bev_fake_alert': 9, 'bev_distribute_virus': 9, 'bev_keep_alive': 9, 'bev_disturb': 9, 'bev_force': 9, 'bev_hinder_app': 9, 'bev_enable_debug': 9, 'bev_malicious_fee': 9, 'bev_virus': 9, 'bev_display_bkg': 9, 'bev_resident_notification': 9, 'bev_outside_ad': 9, 'bev_hard_uninstall': 9, 'bev_cross_access': 9, 'bev_hot_update': 9, 'bev_root': 9, 'prv_start_policy': 9, 'prv_policy_codepage': 9, 'prv_auth_withdraw': 9, 'prv_account_manage': 9, 'prv_data_manage': 9, 'prv_permission_manage': 9, 'prv_authorize_data': 9, 'prv_refuse_authorize': 0, 'prv_apply_repeat': 9, 'prv_authorize_check': 9, 'prv_privacy_virus': 9, 'prv_multi_icon': 9, 'prv_bkg_collect': 9, 'prv_default_app': 9, 'prv_apply_onetime': 9, 'prv_policy_delay': 9, 'prv_match_app': 9, 'prv_match_function': 9, 'prv_match_policy': 9}
    parse_json(res1,res2)