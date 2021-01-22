import unittest

import ddt
import requests
import json

from common.db_handler import cursor
from common.excel_handler import excel
from common.loger_handler import mylog
from common.setting import Config


@ddt.ddt
class TestInnerIssueAPI(unittest.TestCase):
    test_data = excel.read('InnerIssueAPI')

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_inner_issue_api(self, test_data):
        mylog.info('test data{}'.format(test_data))
        url = Config.auto_http + test_data['url']
        method = test_data['method']

        # 暂时使用固定的数据
        data_json = json.loads(test_data['json'])

        # # select from devices，用数据库的数据替换占位数据
        # result = cursor.query("select device_group, req_id, device_id, id, expired_at from task ")
        #
        # data_json = eval(temp_json.replace("#r_i", result[0]).replace("#d_i", result[1]).replace("#i", str(result[2])))

        res = None

        if method.upper() == 'GET':
            try:
                mylog.info("url=====" + url)
                res = requests.get(url=url, params=None, cookies=None)
            except Exception as e:
                mylog.error('request -get error the reason is {}'.format(e))
        elif method.upper() == 'POST':
            try:
                mylog.info("url=====" + url)
                mylog.info("data_json==")
                mylog.info(data_json)
                res = requests.post(url=url, data=None, json=data_json, cookies=None)
            except Exception as e:
                mylog.error('request -post error the reason is {}'.format(e))
        else:
            mylog.error('request method error')

        result = None

        mylog.info('test result{}'.format(res.text))
        try:
            self.assertEqual(test_data['expected'], res.json()['err_code'])
            result = 'success'
        except Exception as e:
            mylog.error('assertion error,res is{}'.format(e))
            result = 'fail'
            raise e
        finally:
            excel.write('InnerIssueAPI', test_data['case_id'] + 1, 9, str(res.json()))
            excel.write('InnerIssueAPI', test_data['case_id'] + 1, 10, result)
