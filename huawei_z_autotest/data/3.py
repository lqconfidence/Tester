#！/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__  = antiy

from common.handle_xlsx import HandleXlsx
import jsonpath
# data={"data":[{"conformance_result":{},"md5":"ecb4b07e336053e3279444b40813482c","secret_result":{}}],"err_code":1620000,"err_msg":""}
#
# # print(jsonpath.jsonpath(data,"$..conformance_result.bev_illegal_content.data[0].bitmap_path"))
# r=jsonpath.jsonpath(data,"$..conformance_result")
# print(r)
# if r:
#     print("ture")

# handle_excel = HandleXlsx("callback_public.xlsx")
# rows = handle_excel.get_rows_values(1)
# print(rows)

data={"data":[{"conformance_result":{"bev_bundle_download":{"data":[],"state":"comply"},"bev_cross_access":{"data":[],"state":"comply"},"bev_display_bkg":{"data":[],"state":"comply"},"bev_distribute_virus":{"data":[],"state":"comply"},"bev_disturb":{"data":[],"state":"comply"},"bev_enable_debug":{"data":[],"state":"comply"},"bev_fake_alert":{"data":[],"state":"comply"},"bev_force":{"data":[],"state":"comply"},"bev_hard_uninstall":{"data":[],"state":"comply"},"bev_hinder_app":{"data":[],"state":"comply"},"bev_hot_update":{"data":[{"virus":["Application/Android.Kotlin.a[app,gen]\u0026Application/Android.RePlugin.a[app,gen]"]}],"state":"violate"},"bev_illegal_content":{"data":[],"state":"comply"},"bev_keep_alive":{"data":[],"state":"comply"},"bev_malicious_fee":{"data":[],"state":"comply"},"bev_outside_ad":{"data":[],"state":"comply"},"bev_resident_notification":{"data":[],"state":"comply"},"bev_root":{"data":[],"state":"comply"},"bev_virus":{"data":[],"state":"comply"},"err_code":1000,"err_msg":"request successed! [detail:process succeeded]"},"md5":"3f91a86e4f3f54d3b61252e2794d8998","secret_result":{"dynamic_err_code":1000,"dynamic_err_msg":"request successed! [detail:process succeeded]","privacy_err_code":1501,"privacy_err_msg":"task error! [detail:crawler failed]","prv_account_manage":{"data":[],"state":"comply"},"prv_apply_dynamic":{"data":[],"state":"comply"},"prv_apply_onetime":{"data":[],"state":"comply"},"prv_apply_repeat":{"data":[],"state":"notexec"},"prv_auth_withdraw":{"data":[],"state":"comply"},"prv_authorize_check":{"data":[],"state":"comply"},"prv_authorize_data":{"data":[],"state":"notexec"},"prv_bkg_collect":{"data":[],"state":"comply"},"prv_data_manage":{"data":[],"state":"comply"},"prv_default_app":{"data":[],"state":"comply"},"prv_is_privacy":{"data":[],"state":"notexec"},"prv_match_app":{"data":[],"state":"notexec"},"prv_match_function":{"data":[],"state":"notexec"},"prv_match_policy":{"data":[],"state":"notexec"},"prv_multi_icon":{"data":[],"state":"comply"},"prv_permission_manage":{"data":[],"state":"comply"},"prv_policy_codepage":{"data":[],"state":"notexec"},"prv_policy_content":{"data":[],"state":"notexec"},"prv_policy_delay":{"data":[],"state":"comply"},"prv_privacy_virus":{"data":[],"state":"comply"},"prv_refuse_authorize":{"data":[],"state":"comply"},"prv_start_policy":{"data":[],"state":"comply"}}}],"err_code":1620000,"err_msg":""}
print(type(data))
res1=jsonpath.jsonpath(data,"$..secret_result")
print(res1)