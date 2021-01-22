import os


class Config:
    # root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root_path = os.path.realpath(__file__)
    print(root_path)
    # data_path = os.path.join(root_path,'data','cases.xlsx')
    data_path = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'cases.xlsx')

    log_path = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'loger', 'log_container')
    print(log_path)
    # case_path = os.path.join(root_path,r"testcases")
    case_path = os.path.join(os.path.split(os.path.split(root_path)[0])[0], "testcases")
    # config_path  = os.path.join(root_path,'common','config_test.ini')
    config_path = os.path.join(os.path.split(root_path)[0], 'config_test.ini')
    # report_path = os.path.join(root_path,"report")
    report_path = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'report')
    # excel_path=os.path.join(root_path,"data",'case.xlsx')
    excel_path = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'case.xlsx')
    excel_download = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'download.xlsx')
    excel_ppcawler = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'ppcrawler.xlsx')
    excel_static_privacy = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'static_privacy.xlsx')
    excel_callback_public = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'callback_public.xlsx')
    excel_prod_public = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'prod_public.xlsx')
    excel_analog = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'analog.xlsx')
    excel_hw_privacyreview_case = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'privacyreview_case.xlsx')
    excel_hw_privacyreview_all = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'privacyreview_all.xlsx')
    excel_hw_zhongduan = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'pa_inspection_hwzp_task_id.xlsx')
    excel_function_app = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'prv_match_function.xlsx')
    excel_aosp = os.path.join(os.path.split(os.path.split(root_path)[0])[0], 'data', 'analog.xlsx')
    # 数据库参数
    db_host = "192.168.65.67"
    db_port = 3306
    db_user = "analog"
    db_password = "analog"
    db_charset = "UTF8"
    db_database = "analog_inspection_test"

    # 自动化模块地址
    auto_http = "http://analog-inspection.d.k8ss.cc"

    # 语义分析地址
    words_analysis_http = "http://privacy-terms-review.dev.k8ss.cc"

    # 签名
    Sign = "xxxxxxxxx"

    @staticmethod
    def create(self):
        if not os.path.exists(self.report_path):
            os.mkdir(self.report_path)

    #log_path = os.path.join(os.path.split(root_path)[0], 'loger', "log_container")

    @classmethod
    def createreport(cls):
        if not os.path.exists(cls.log_path):
            os.mkdir(cls.log_path)
    # yaml_config_path = os.path.join(config_path,"config.yaml")

#print(Config.log_path)
