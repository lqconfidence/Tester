import unittest
import ddt
from common.loger_handler import mylog
import json
import requests
import time
import jsonpath


from common.excel_handler import excel_app_function

from common.sheet_header import SheetHeader

sheet_name = "prv_match_app"
head_data = excel_app_function.header(sheet_name)
sheet_head = SheetHeader(head_data)
#sheet_column = sheet_head.__dict__
print("-----------------------sheet_head类型为{}---值为{}".format(type(sheet_head),sheet_head.__dict__))
test_datas = excel_app_function.read(sheet_name)

@ddt.ddt
class TestMatchFunction(unittest.TestCase):

    @ddt.data(*test_datas)
    def test_match_app(self, test_data):
        res_prv_match_app = json.loads(test_data['prv_match_app'])
        print(res_prv_match_app,type(res_prv_match_app))
        case_data = json.loads(test_data['case_data'])
        row = test_data['case_id']+1
        print(case_data,type(case_data))
        case_data_app = case_data['prv_match_app']
        tmp_premission = case_data_app['permission']
        tmp_userdata = case_data_app['userdata']
        res_permission = []
        res_userdata = []

        if 'permission' in str(res_prv_match_app['data']):
            res_permission = res_prv_match_app['data'][0]['permission']
        if 'userdata' in str(res_prv_match_app['data']):
            res_userdata = res_prv_match_app['data'][0]['userdata']
        print("===============================================================================")
        print("casedata的所有permission和userdata", tmp_premission, tmp_userdata)
        print("实际结果的permission和userdata", res_permission, res_userdata)
        print("===============================================================================")
        for k in tmp_premission:
            if k in str(res_permission):
                print(k,"在证据中存在")
                excel_app_function.write(sheet_name,row=row,column=sheet_head.__getattribute__('assert_permission'),data="实际结果存在{}".format(k))
                break
        for j in tmp_userdata:
            if j in str(res_userdata):
                print(j,"在证据中存在")
                excel_app_function.write(sheet_name,row=row,column=sheet_head.__getattribute__('assert_userdata'),data="实际结果存在{}".format(j))
                break



if __name__ == '__main__':
    unittest.main()

