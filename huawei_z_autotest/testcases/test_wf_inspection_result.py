
import unittest

import ddt
import requests
import jsonpath
import json

import time
from common.excel_handler import excel_callback_public
from common.loger_handler import mylog
from common.sheet_header import SheetHeader
sheet_name = 'wf_inspection'
head_data = excel_callback_public.header(sheet_name)
sheet_head = SheetHeader(head_data)
#sheet_column = sheet_head.__dict__
print("-----------------------sheet_head类型为{}---值为{}".format(type(sheet_head),sheet_head.__dict__))
@ddt.ddt
class TestInnerIssueAPI(unittest.TestCase):
    test_data = excel_callback_public.read(sheet_name)


    def setUp(self) -> None:
        mylog.info('test starting')
        pass

    def tearDown(self) -> None:
        mylog.info('test finished')
        pass

    @ddt.data(*test_data)
    def test_optputs_wf(self, test_data):
        ip = "http://workflow-cp-fe.test.k8ss.cc"
        mylog.info('test data{}'.format(test_data))
        url = ip + test_data['path']
        method = test_data['method']
        task_id = test_data['task_id']
        case_id = test_data['case_id']
        # 请求参数
        request_body = {"query":"query task($taskId: String!)\n{  task(taskId: $taskId) \n  {   \n  app\n  completedAt  \n  createdAt    \n  expiredAt   \n  priority     \n  taskId   \n \n  outputs \n  updatedAt   \n  }\n}",
                        "variables":{"taskId":task_id},"operationName":"task"}
        headers = {'Authorization':'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkc3AiOiIlRTYlQUMlQTclRTklOTglQjMlRTklOTQlOTAiLCJlbWwiOiJvdXlhbmdydWlAYW50aXkuY24iLCJleHAiOjE1OTQ2MjY4MDMsIm5iZiI6MTU5NDY'
                                   'wNDkwMywidWlkIjoib3V5YW5ncnVpMSJ9.JTEQ2HPGckX3sriv6UvcBSbIjnCPyGyQ4OO6WHRcDq0'}
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
                mylog.info(request_body)
                res = requests.post(url=url, data=None, json=request_body, cookies=None, headers=headers)
            except Exception as e:
                mylog.error('request -post error the reason is {}'.format(e))
        else:
            mylog.error('request method error')

        header_obj = {}

        #用例执行结果
        result = None



        # 解析outputs
        outputs = jsonpath.jsonpath(res.json(), '$..outputs')
        print(*outputs, type(*outputs))
        outputs_json = json.loads(*outputs)

        ###查找任务基本信息######
        # 查找create_at，保留输入值[任务创建时间]
        createdAt = jsonpath.jsonpath(res.json(), '$..createdAt')[0]
        # 查找init的MD5，保留输入值
        init_md5 = jsonpath.jsonpath(outputs_json, '$.init.md5')[0]
        # 查找init的trace_id，保留输入值
        trace_id = jsonpath.jsonpath(outputs_json, '$.init.trace_id')[0]
        # 查找init的apk_url，保留输入值
        apkUrl = jsonpath.jsonpath(outputs_json, '$.init.apkUrl')[0]
        # 查找init的privacyUrl，保留输入值
        privacyUrl = jsonpath.jsonpath(outputs_json, '$.init.privacyUrl')
        #print(info, type(info))
        #####查找任务关键信息###########

        # 查找download的MD5字段，用于判断下载是否成功
        md5 = jsonpath.jsonpath(outputs_json, '$.downloader.data.md5')
        print("*********************download的MD5为{}".format(md5))
        # 查找爬虫返回的status，用于判断爬虫是否成功
        ppcrawler_status = jsonpath.jsonpath(outputs_json, '$..status')
        # 查找prv_is_privacy，用于判断是否是隐私。若值的长度大于1，就认为是隐私
        prv_is_privacy = jsonpath.jsonpath(outputs_json, '$..prv_is_privacy')
        # 查找privacyreview，用于判断语义分析是否执行完。若为null，则认为服务异常或者分析超时
        privacyreview = jsonpath.jsonpath(outputs_json, '$..privacyreview')
        print("********测试测试测试privacyreview*****{}".format(privacyreview))

        mylog.info('test result{}'.format(res.text))
        try:
            if md5 == False:
                excel_callback_public.write(sheet_name, case_id + 1, column=sheet_head.__getattribute__('downloader'),
                                            data="下载异常")
            else:
                excel_callback_public.write(sheet_name, case_id + 1, column=sheet_head.__getattribute__('downloader'),
                                            data="下载成功")
                if ppcrawler_status == False:
                    excel_callback_public.write(sheet_name, case_id + 1,
                                                column=sheet_head.__getattribute__('ppcrawler'),
                                                data="没有找到爬虫的status")

                elif ppcrawler_status[0] != 'success':
                    excel_callback_public.write(sheet_name, case_id + 1,
                                                column=sheet_head.__getattribute__('ppcrawler'),
                                                data="爬虫失败")
                else:
                    excel_callback_public.write(sheet_name, case_id + 1,
                                                column=sheet_head.__getattribute__('ppcrawler'),
                                                data="爬虫成功")
                    if privacyreview == False:
                        excel_callback_public.write(sheet_name, case_id + 1,
                                                    column=sheet_head.__getattribute__('privacyreview'),
                                                    data="语义分析失败,结果没有privacyreview")
                    elif privacyreview[0] == 'null':
                        excel_callback_public.write(sheet_name, case_id + 1,
                                                    column=sheet_head.__getattribute__('privacyreview'),
                                                    data="语义分析超时")
                    else:
                        excel_callback_public.write(sheet_name, case_id + 1,
                                                    column=sheet_head.__getattribute__('privacyreview'),
                                                    data="语义分析成功")
                        print("****************privacyreview****值为{}".format(privacyreview[0]),type(privacyreview[0]))
                        if len(prv_is_privacy[0]) < 1:
                            excel_callback_public.write(sheet_name, case_id + 1,
                                                        column=sheet_head.__getattribute__('prv_is_privacy'),
                                                        data="不是隐私政策")
                        else:
                            excel_callback_public.write(sheet_name, case_id + 1,
                                                        column=sheet_head.__getattribute__('prv_is_privacy'),
                                                        data="是隐私政策")


        except Exception as e:
            mylog.error('assertion error,res is{}'.format(e))

            raise e
        finally:
            excel_callback_public.write(sheet_name, case_id + 1, column=sheet_head.__getattribute__('apkUrl'),
                                        data=apkUrl)
            excel_callback_public.write(sheet_name, case_id + 1, column=sheet_head.__getattribute__('init_md5'),
                                        data=init_md5)
            if privacyUrl == False:
                excel_callback_public.write(sheet_name, case_id + 1, column=sheet_head.__getattribute__('privacyUrl'),
                                            data='未传privacyUrl')
            else:
                excel_callback_public.write(sheet_name, case_id + 1, column=sheet_head.__getattribute__('privacyUrl'),
                                            data=privacyUrl[0])

            excel_callback_public.write(sheet_name, case_id + 1, column=sheet_head.__getattribute__('trace_id'),
                                        data=trace_id)
            excel_callback_public.write(sheet_name, case_id + 1, column=sheet_head.__getattribute__('createdAt'),
                                        data=createdAt)








