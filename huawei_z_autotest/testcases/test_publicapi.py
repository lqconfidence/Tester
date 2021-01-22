#外网，已写完

import unittest
from common.excel_handler import excel_callback_public
from common.encryption_publicapi import encryption
from common.loger_handler import mylog
from libs.ddt import ddt, data
from common.yaml_handler import myconf
from common.pubic_testdata_handler import HandlerPublicTestData


@ddt
class PublicApi(unittest.TestCase):
    test_datas =excel_callback_public.read('publicapi_hwa')
    hpt = HandlerPublicTestData()

    def setUp(self) -> None:
        mylog.info('test start')

    def tearDown(self) -> None:
        mylog.info('test finished')

    @data(*test_datas)
    def test_public_api(self, test_data):
        print(test_data)
        print(type(test_data))
        mylog.info('test data is :{}'.format(test_data))
        url = test_data['url']
        print(url,type(url))
        ip = myconf.get('public_api','ip')
        method = test_data['method']
        tpl = test_data['tpl']
        sk = test_data['sk']
        case_id = test_data['case_id']
        expected = test_data['expected']
        sql = "select task_id from `public_api_test`.tasks  WHERE type='compliance' ORDER BY created_at ASC"
        sql1 = "select md5 from `public_api_test`.tasks  WHERE type='compliance' ORDER BY created_at ASC"
        task_id = "#task_id#"
        md5 = "#md5#"
        request_body = self.hpt.handler_test_data(test_data['json'],sql=sql,before_str=task_id)
        request_body = self.hpt.handler_test_data(request_body, sql=sql1,before_str=md5)
        print(request_body)
        res = encryption(ip=ip,path=url, method=method, tpl=tpl, secret_key=sk, request_body=request_body)
        actual = res.json()['err_code']
        result = None
        try:
            self.assertEqual(expected, actual)
            result = "success"
        except Exception as e:
            mylog.error("test failed {}".format(e))
            result = "failed"
            raise e
        finally:
            mylog.info('actual result is{}'.format(res.json()))
            excel_callback_public.write('publicapi_hwa', case_id + 1, 10, str(res.json()))
            excel_callback_public.write('publicapi_hwa', case_id + 1, 11, result)


if __name__ == '__main__':
    unittest.main()
