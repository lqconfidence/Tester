import unittest
import os
import time
from common.setting import Config
from libs.HTMLTestRunnerNew import HTMLTestRunner

test_case = Config.case_path
save_report = Config.report_path
now = time.strftime('%Y-%m-%d')
path = os.path.join(save_report, 'report_{}.html'.format(now))
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.discover(test_case))
with open(path, 'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            verbosity=2,
                            title="huawei_Z",
                            description="api_test_result",
                            tester='ouayngrui')
    runner.run(suite)
