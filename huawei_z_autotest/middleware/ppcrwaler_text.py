# -*-coding:utf-8 -*-
# @Time:2020/8/12 13:47
# @Author:a'nan
# @Email:934257271
# @File:ppcrwaler_text.py

import requests
import time
import jsonpath
import chardet


class MidPpcrawler:
    def Ppcrawler(privacy_url):
        print("进入函数")
        url = "http://crawler.t.k8ss.cc/task/create"
        request_id = int(time.time())
        request_body = {"urls": [privacy_url],
                      "requestId": str(request_id)}
        print(request_body)
        header = {'Content-Type':'application/json;charset=UTF-8'}
        res = requests.post(url=url, json=request_body, headers=header)
        text = jsonpath.jsonpath(res.json(), "$..text")
        text1 = ''
        if text == False:
            text1 = '没有找到text字段，爬虫失败了'
        else:
            text1 = text[0]

        #print(text1)
        return text1


if __name__ == "__main__":

    res = MidPpcrawler.Ppcrawler("https://pass.hujiang.com/agreement111")
    print("爬虫原始结果及类型\n"+res)
    print(type(res))
    res1 = res.encode()
    print("endoce之后的类型")
    print(res1, type(res1))
    res2 = res1.decode('utf-8')
    print("decode为Unicode之后的类型")
    print(res2,type(res2))


