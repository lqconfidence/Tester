import unittest
import ddt
import yaml
from common.excel_handler import excel
from common.loger_handler import mylog
# from common.request_handler import Http
from common.setting import Config
from common import request_handler
from common.yaml_handler import myconf


@ddt.ddt
class Test_Keyword(unittest.TestCase):
    testdata = excel.read('keywordlist')

    def setUp(self) -> None:
        mylog.info('test starting')

    def tearDown(self) -> None:
        mylog.info('test finished')

    @ddt.data(*testdata)
    def test_keyword_list(self, test_data):
        # print("======================================")
        mylog.info('test data{}'.format(test_data))
        # mylog.info("======================================")
        url = test_data['url']
        method = test_data['method']

        res = request_handler.Http(url, method).http()
        result = None
        mylog.info('test result{}'.format(res.text))
        try:

            self.assertEqual(test_data['expected'], res.json()['meta']['errCode'])
            result = 'success'
        except Exception as e:
            mylog.error('assertion error,reson is{}'.format(e))
            result = 'fail'
            raise e
        finally:
            excel.write('keywordlist', test_data['case_id'] + 1, 9, str(res.json()))
            excel.write('keywordlist', test_data['case_id'] + 1, 10, result)
