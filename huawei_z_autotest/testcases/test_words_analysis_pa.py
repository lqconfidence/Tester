"""
外网投放apk样本，进行数据库查询或者外网模块查询是否有检出各项语义分析case,如果有把结果写入表格中
分析：目前语义分析比较缓慢，暂定20分钟出一个结果，需要不上班的时候进行语义分析的定时投放，第二天进行通过外网模块，用md5查询
1.准备数据，taskid/md5，
2.接口准备：pa投放接口接口，使用的是代理工具接口需要添加header，header中填写投放地址
3.接口准备：pa查询接口，使用md5查询，这里可能需要开启另外一个线程去查询，具体怎么做--待学习
4.返回写入表格是否为隐私文本值 prv_is_privacy
5.接口返回数据与case项匹配是否检出，检出则写入表中（一定要写入吗？可以不写，值为：检出或者检出+case值）prv_policy_content
"""
import unittest
import ddt
import requests
from common.excel_handler import excel_analysis_pa
from common.loger_handler import mylog
from common.request_handler import Http
import jsonpath
import json
import time
sheet_name = "Sheet1"


@ddt.ddt
class TestWordsAnalysis(unittest.TestCase):
    test_data = excel_analysis_pa.read(sheet_name)
    head_data = excel_analysis_pa.header(sheet_name)

    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_words_analysis(self, test_data):

        header_obj = {}
        for i in range(len(self.head_data)):
            header_obj[self.head_data[i]] = i+1

        print("test---------------------{}".format(header_obj))


        mylog.info('test case{}'.format(test_data))
        request_url = "http://utils-signature-proxy.d.k8ss.cc/v1/task/status?tpl=hw-z-p"
        md5 = test_data['md5']
        data_json = {
            "request":[
                {
                    "md5":md5,
                    "type": ["secret"]
                }
            ]
        }
        headers = {'X-HOST': 'public-api.d.k8ss.cc', 'X-PORT': '80', 'X-SK': 'testtest', 'Content-Type': 'application/json'}
        res = Http(request_url, "post", json.dumps(data_json), headers=headers).http()  # 执行请求
        is_privacy = jsonpath.jsonpath(res.json(), '$..prv_is_privacy.state')
        content = jsonpath.jsonpath(res.json(), '$..prv_policy_content')[0]["data"]

        print("是否隐私=={}".format(str(is_privacy)))
        print("prv_policy_content结果=={}".format(str(content)))
        keys = [key["type"] for key in content]
        print("keys==={}".format(keys))

        try:
            st = time.time()
            for case in content:

                cell_idx = int(header_obj.get(case.get("type")))
                state = str(case.get("state"))
                types = str(case.get("type")) + ":"
                data = str(case.get("data"))
                print("{}=={}".format(case.get("type")+str(cell_idx), case.get("data")))
                excel_analysis_pa.write(sheet_name, test_data['case_id'] + 1,cell_idx , types + state + data)
            et = time.time()
            print("cost time==={}".format(et-st))


        except Exception as e:
            mylog.error('assertion error,res is {}'.format(e))
            raise e
        finally:
            # print("is_privacy =={}".format(str(is_privacy)))
            excel_analysis_pa.write(sheet_name, test_data['case_id'] + 1, 5, str(is_privacy))


if __name__ == '__main__':
    unittest.main()

