import unittest
import ddt

from common import request_handler
from common.excel_handler import excel
from common.loger_handler import mylog


@ddt.ddt
class TestDeviceListQuery(unittest.TestCase):
    test_data = excel.read('DeviceListQuery')

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_device_list_query(self, test_data):
        mylog.info('test data{}'.format(test_data))
        url = test_data['url']
        method = test_data['method']
        res = request_handler.Http(url, method).http()
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
            excel.write('DeviceListQuery', test_data['case_id'] + 1, 9, str(res.json()))
            excel.write('DeviceListQuery', test_data['case_id'] + 1, 10, result)
