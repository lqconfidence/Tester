#曾祥文写的
import unittest

import ddt
import requests

from common.excel_handler import excel
from common.loger_handler import mylog
from common.setting import Config
from common.text_handler import TextHandler


@ddt.ddt
class TestWordsAnalysis(unittest.TestCase):
    test_data = excel.read('WordsAnalysis')

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_words_analysis(self, test_data):
        mylog.info('test data{}'.format(test_data))
        url = Config.words_analysis_http + test_data['url']
        method = test_data['method']
        file = test_data['file']
        check_type = eval(test_data['type'])

        # mylog.info的类型为string
        temp_json = test_data['json']

        # 读取html文件
        text_result = TextHandler(file).clean_html_custom()
        data_json = eval(temp_json.replace("#f_p", text_result))

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
                res = requests.post(url=url, data=None, json=data_json, cookies=None)
            except Exception as e:
                mylog.error('request -post error the reason is {}'.format(e))
        else:
            mylog.error('request method error')

        result = None
        mylog.info('test result{}'.format(res.text))
        try:
            # res 是一个字典
            # 用于返回有结果的检测项的个数
            flag_1 = 0
            for i in check_type:
                # 遍历检测类型列表，对比返回结果是否都有值
                if res.json()['data']['result'][i]:
                    flag_1 += 1
            # mylog.info("flag_1的值：：")
            # mylog.info(flag_1)
            self.assertEqual(test_data['expected'], flag_1)
            result = 'success'

        except Exception as e:
            mylog.error('assertion error,res is {}'.format(e))
            result = 'fail'
            raise e
        finally:
            excel.write('WordsAnalysis', test_data['case_id'] + 1, 11, str(res.json()))
            excel.write('WordsAnalysis', test_data['case_id'] + 1, 12, result)
