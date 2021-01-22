import unittest

import ddt
import requests

from common.db_handler import cursor
from common.excel_handler import excel
from common.loger_handler import mylog
from common.setting import Config


@ddt.ddt
class TestDeviceHealth(unittest.TestCase):
    test_data = excel.read('DeviceHealth')

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_device_health(self, test_data):
        mylog.info('test data{}'.format(test_data))
        url = Config.auto_http + test_data['url']
        method = test_data['method']

        db_result = cursor.query("select device_id from devices")

        # 不使用request_handler
        # request_obj = request_handler.Http(url, method).http
        res = None
        # if method.upper() == 'GET':
        try:
            # get方式的，将请求参数附加到url后面

            # url = url.replace("#d_i", db_result[0])
            mylog.info("url==========" + url)

            res = requests.get(url=url, params=None, cookies=None)
        except Exception as e:
            mylog.error('request -get error the reason is {}'.format(e))
        # elif method.upper() == 'POST':
        #     try:
        #         mylog.info("data_json==========" + data_json)
        #         res = requests.post(url=url, data=None, json=data_json, cookies=None)
        #         pass
        #     except Exception as e:
        #         mylog.error('request -post error the reason is {}'.format(e))
        # else:
        #     mylog.error('request method error')

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
            excel.write('DeviceHealth', test_data['case_id'] + 1, 9, str(res.json()))
            excel.write('DeviceHealth', test_data['case_id'] + 1, 10, result)
            # excel.write('DeviceStateReset', test_data['case_id'] + 1, 11, url)
