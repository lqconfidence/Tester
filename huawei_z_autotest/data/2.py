#！/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__  = antiy

import jsonpath
from common.handle_xlsx import HandleXlsx
import json
from common.Untils import parse_json
data2={
    "data": [
        {
            "conformance_result": {
                "bev_bundle_download": {
                    "data": [],
                    "state": "violate"
                },
                "bev_cross_access": {
                    "data": [],
                    "state": "violate"
                },
                "bev_display_bkg": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_distribute_virus": {
                    "data": [],
                    "state": "violate"
                },
                "bev_disturb": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_enable_debug": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_fake_alert": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_force": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_hard_uninstall": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_hinder_app": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_hot_update": {
                    "data": [],
                    "state": "violate"
                },
                "bev_illegal_content": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_keep_alive": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_malicious_fee": {
                    "data": [],
                    "state": "violate"
                },
                "bev_outside_ad": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_resident_notification": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "bev_root": {
                    "data": [],
                    "state": "violate"
                },
                "bev_virus": {
                    "data": [
                        {
                            "virus": [
                                "Trojan/Android.GDownload.dz[exp,gen]"
                            ]
                        }
                    ],
                    "state": "violate"
                },
                "err_code": 1000,
                "err_msg": "request successed! [detail:process succeeded]"
            },
            "md5": "1f4cf43865606bd0d468f587084946d7",
            "secret_result": {
                "dynamic_err_code": 1000,
                "dynamic_err_msg": "request successed! [detail:process succeeded]",
                "privacy_err_code": 1501,
                "privacy_err_msg": "task error! [detail:crawler failed]",
                "prv_account_manage": {
                    "data": [],
                    "state": "comply"
                },
                "prv_apply_dynamic": {
                    "data": [],
                    "state": "comply"
                },
                "prv_apply_onetime": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "prv_apply_repeat": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "prv_auth_withdraw": {
                    "data": [],
                    "state": "comply"
                },
                "prv_authorize_check": {
                    "data": [],
                    "state": "violate"
                },
                "prv_authorize_data": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }
],
                    "state": "violate"
                },
                "prv_bkg_collect": {
                    "data": [],
                    "state": "violate"
                },
                "prv_data_manage": {
                    "data": [],
                    "state": "comply"
                },
                "prv_default_app": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "prv_is_privacy": {
                    "data": [],
                    "state": "notexec"
                },
                "prv_match_app": {
                    "data": [],
                    "state": "violate"
                },
                "prv_match_function": {
                    "data": [],
                    "state": "violate"
                },
                "prv_match_policy": {
                    "data": [],
                    "state": "violate"
                },
                "prv_multi_icon": {
                    "data": [],
                    "state": "violate"
                },
                "prv_permission_manage": {
                    "data": [],
                    "state": "comply"
                },
                "prv_policy_codepage": {
                    "data": [],
                    "state": "comply"
                },
                "prv_policy_content": {
                    "data": [],
                    "state": "notexec"
                },
                "prv_policy_delay": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "violate"
                },
                "prv_privacy_virus": {
                    "data": [],
                    "state": "violate"
                },
                "prv_refuse_authorize": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "comply"
                },
                "prv_start_policy": {
                    "data": [{
              "bitmap_path": [
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673699689.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673812434.jpg",
                "http://hwa-snapshot.avlyun.com/sign/96fc6122-a021-4d13-aa55-8544e8d66649_2a11f8918ba66799324fb1e5a07fee0c_prv_authorize_data_1607673697347.jpg"
              ],
              "userdata": [
                "applist",
                "sms",
                "gps",
                "sn",
                "deviceid",
                "mac"
              ]
            }],
                    "state": "comply"
                }
            }
        }
    ],
    "err_code": 1620000,
    "err_msg": ""
}


# a=jsonpath.jsonpath(data2,"$..secret_result.prv_authorize_data.data[0].bitmap_path")
# print(a)


data3={"data":[{"conformance_result":{},"md5":"3f91a86e4f3f54d3b61252e2794d8998","secret_result":{}}],"err_code":1620000,"err_msg":""}
if __name__=="__main__":
    print(jsonpath.jsonpath(data3, "$..conformance_result"))
    print(jsonpath.jsonpath(data3, "$..secret_result"))

    parse_json(data3,2)
    # def parse_json():
    #     h=HandleXlsx('callback_public.xlsx')
    #     res1=jsonpath.jsonpath(data2,"$..secret_result")[0]
    #     res2=jsonpath.jsonpath(data2,"$..conformance_result")[0]
    #     res=dict(res1,**res2)
    #     print(res)
    #     n=1
    #     for key,value in res.items():
    #         n+=1
    #         h.excel_write_data(1, 15+n, key)
    #         h.excel_write_data(2, 15+n, str(value))


