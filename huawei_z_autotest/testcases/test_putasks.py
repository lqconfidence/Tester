from common.Untils import *
import unittest
import ddt
import threading

handle_excel = HandleXlsx("callback_public.xlsx")
data = handle_excel.get_excel_data()

@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        res1 = calculateCheckoutRate()
        res2 = calculateCaptureRate()
        parse_json(res1,res2)

    @ddt.data(*data)
    def test_main_case(self,data):
        case_id=data[0]
        rownum = handle_excel.get_row_numbr_with_caseID(case_id)
        apk_url = data[1]
        privacyurl = data[2] if data[2] else ''
        md5 = data[3]
        apptype = data[4] if data[4] else ''
        flag = data[5] if data[5] else ''
        introduction = data[6] if data[6] else ''
        request_body={ "request": [{"md5": md5,
                        "url": apk_url,
                        "type": ["secret", "conformance"],
                        "options": {
                            "secret": {
                                     "apptype": apptype,
                                     "introduction": introduction,
                                     "flag": flag,
                                     "privacyurl": privacyurl
                                        }
                                             }
                                                 }]
                       }

        print("当前case_id is {}".format(case_id))
        try:
            task_id = post_hw_task(request_body)
            t1=threading.Thread(target=get_hw_result,args=(task_id,rownum))
            t1.run()

            put_rate(case_id,5,900)

        except Exception as e:
            print('request -post error the reason is {}'.format(e))
            raise e

if __name__=="__main__":
    unittest.main()
