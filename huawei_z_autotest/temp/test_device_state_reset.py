import unittest
import ddt
import requests

from common import request_handler
from common.db_handler import cursor
from common.excel_handler import excel
from common.loger_handler import mylog
from common.setting import Config


@ddt.ddt
class TestDeviceStateReset(unittest.TestCase):
    test_data = excel.read('DeviceStateReset')

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_device_state_reset(self, test_data):
        mylog.info('test data{}'.format(test_data))
        url = Config.auto_http + test_data['url']
        method = test_data['method']

        # mylog.info的类型为string


        # select from devices，用数据库的数据替换占位数据
        db_result = cursor.query("select device_id from devices")
        # data_json = eval(temp_json.replace("#d_i", db_result[0]))

        # mylog.info("data_json=========" + data_json)

        # 不使用request_handler
        # request_obj = request_handler.Http(url, method).http
        res = None
        if method.upper() == 'GET':
            try:
                # get方式的，将请求参数附加到url后面
                url = url.replace("#d_i", db_result[0])
                # mylog.info("temp_url==========" + temp_url)

                # url = temp_url.replace("\"", "")
                mylog.info("url==========" + url)

                res = requests.get(url=url, params=None, cookies=None)
            except Exception as e:
                mylog.error('request -get error the reason is {}'.format(e))
        elif method.upper() == 'POST':
            try:

                res = requests.post(url=url, data=None, json=None, cookies=None)
                pass
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
            excel.write('DeviceStateReset', test_data['case_id'] + 1, 9, str(res.json()))
            excel.write('DeviceStateReset', test_data['case_id'] + 1, 10, result)
            # excel.write('DeviceStateReset', test_data['case_id'] + 1, 11, url)
