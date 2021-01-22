import unittest
import ddt
from common.loger_handler import mylog
import json
import requests
import time
import jsonpath


from common.excel_handler import excel_app_function

from common.sheet_header import SheetHeader

sheet_name = "prv_match_function"
head_data = excel_app_function.header(sheet_name)
sheet_head = SheetHeader(head_data)
#sheet_column = sheet_head.__dict__
print("-----------------------sheet_head类型为{}---值为{}".format(type(sheet_head),sheet_head.__dict__))
test_datas = excel_app_function.read(sheet_name)

@ddt.ddt
class TestMatchFunction(unittest.TestCase):

    @ddt.data(*test_datas)
    def test_status_pa_prv(self, test_data):
        res_prv_match_function = json.loads(test_data['prv_match_function'])
        #print(res_prv_match_function,type(res_prv_match_function))
        case_data = json.loads(test_data['case_data'])
        row = test_data['case_id']+1
        #print(case_data,type(case_data))
        case_data_fun = case_data['prv_match_function']
        tmp_premission = []
        for i in case_data_fun:
            for j in i['permission']:
                tmp_premission.append(j)
        res_permission = []
        if 'permission' in str(res_prv_match_function['data']):
            res_permission = res_prv_match_function['data'][0]['permission']
        print("===============================================================================")
        print("casedata的所有permission",tmp_premission,type(tmp_premission))
        print("实际结果的permission",res_permission,type(res_permission))
        print("===============================================================================")
        for k in tmp_premission:
            print(k)
            if k in str(res_permission):
                print(k,"在证据中存在")
                excel_app_function.write(sheet_name,row=row,column=sheet_head.__getattribute__('assert_permission'),data="实际结果存在{}".format(k))
                break



if __name__ == '__main__':
    unittest.main()

