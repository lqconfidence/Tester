# -*-coding:utf-8 -*-
# @Time:2020/5/8 17:53
# @Author:a'nan
# @Email:934257271
# @File:jiexi.py
import json

info = [[{'data': [], 'type': 'global_broadcast', 'state': False}, {'data': [], 'type': 'lock_screen_ad', 'state': False}, {'data': [], 'type': 'mulite_icon', 'state': False}, {'data': None, 'type': 'privacy_text', 'state': False}, {'data': [], 'type': 'suspected_privacy_activity', 'state': True}, {'data': [], 'type': 'other_activity', 'state': False}]]

print(*info)


import  time
print(int(time.time()))
req = {'task_id': 'd8709db0-41e3-462e-a6aa-111111111111', 'app_id': 'vivo-test', 'priority': 1, 'options': {'apkUrl': 'https://swsdl.vivo.com.cn/appstore/ad/apk/20200419/2020041901232470143.apk', 'md5': '97381bce37856566638c9a5c9abff793'}}
print(req,type(req))
print(json.dumps(req),type(json.dumps(req)))