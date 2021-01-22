import unittest

import ddt
import requests

from common.db_handler import cursor
from common.excel_handler import excel
from common.loger_handler import mylog
from common.setting import Config


@ddt.ddt
class TestTaskStop(unittest.TestCase):
    test_data = excel.read('TaskStop')

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_task_stop(self, test_data):
        mylog.info('test data{}'.format(test_data))
        url = Config.auto_http + test_data['url']
        method = test_data['method']

        # mylog.info的类型为string
        temp_json = test_data['json']

        # select from devices，用数据库的数据替换占位数据
        result = cursor.query("select req_id from task")
        mylog.info("data_json====" + temp_json.replace("#r_i", result[0]))
        data_json = eval(temp_json.replace("#r_i", result[0]))

        # 不使用request_handler
        # request_obj = request_handler.Http(url, method).http
        res = None

        if method.upper() == 'GET':
            try:
                res = requests.get(url=url, params=None, cookies=None)
            except Exception as e:
                mylog.error('request -get error the reason is {}'.format(e))
        elif method.upper() == 'POST':
            try:
                mylog.info("url=========" + url)
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
            mylog.error('assertion error,res is {}'.format(e))
            result = 'fail'
            raise e
        finally:
            excel.write('TaskStop', test_data['case_id'] + 1, 9, str(res.json()))
            excel.write('TaskStop', test_data['case_id'] + 1, 10, result)
