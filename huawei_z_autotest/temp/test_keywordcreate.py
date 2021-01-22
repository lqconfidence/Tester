import json
import unittest
import ddt
import yaml
from common.excel_handler import excel
from common.loger_handler import mylog
from common.request_handler import Http
from common.setting import Config
from common.yaml_handler import myconf
from middleware.list_middware import List


@ddt.ddt
class Test_Keyword_create(unittest.TestCase):
    testdata = excel.read('keywordcreate')

    @classmethod
    def setUpClass(cls) -> None:
        mylog.info('test starting')

    @classmethod
    def tearDownClass(cls) -> None:
        mylog.info('test finished')

    @ddt.data(*testdata)
    # 单条字典
    def test_keyword_list(self, test_data):
        be_num = List().id()
        # print(test_data)
        mylog.info('test data{}'.format(test_data))
        url = test_data['url']
        method = test_data['method']
        param = json.loads(test_data['json'])
        # print(type(param))

        res = Http(url, method, param).http()
        result = None
        if res.json()['meta']['errCode'] == 0:
            af_num = List().id()
            try:
                self.assertEqual(be_num + 1, af_num)
            except Exception as e:
                mylog.error('id_assertion_error,reson is{}'.format(e))
        mylog.info('test result{}'.format(res.text))
        try:
            self.assertEqual(test_data['expected'], res.json()['meta']['errCode'])
            result = 'success'
        except Exception as e:
            mylog.error('assertion error,reson is{}'.format(e))
            result = 'fail'
            raise e
        finally:
            excel.write('keywordcreate', test_data['case_id'] + 1, 9, str(res.json()))
            excel.write('keywordcreate', test_data['case_id'] + 1, 10, result)
