""""
*************
Author:ouyangrui
Time:2020/4/23
Email:934257271@qq.com
********************
"""
import hashlib
import time
import hmac
import json
import requests


def encryption(ip, path, method, tpl, secret_key, request_body, headers=None):
    #将请求参数加密

    #print(json.dumps(eval(request_body)))
    m = hashlib.md5()
    content_md5 = m.update(request_body.encode("utf8"))
    content_md5 = m.hexdigest()
    #print("长度为{}".format(len(str(eval(request_body)))))
    print("请求参数加密之后的MD5为：{},类型为{}".format(content_md5, type(content_md5)))

    #生成时间戳
    ts = int(time.time())
    print("时间戳为{}".format(ts))

    #构造签名字符串
    signstr = "content_md5={}&method={}&tpl={}&ts={}&url_path={}".format(content_md5,method,tpl,ts,path)
    print("签名字符串为：{}".format(signstr))
    #使用key进行HmacSHA256加密
    signature = hmac.new(bytes(secret_key,encoding='utf-8'),bytes(signstr,encoding='utf-8'),digestmod=hashlib.sha256).digest()
    #二进制转为HEX
    sign = signature.hex()
    print("加密之后的sign为{}".format(sign))
    url = "{}{}?ts={}&tpl={}&sign={}".format(ip,path,ts,tpl,sign)
    print("完整的请求url为{}".format(url))
    #print("请求参数为{},长度为{}".format(eval(reques t_body),len(json.dumps(eval(request_body)))))
    #res = hr.send(url=url,method=method,json=eval(request_body),headers=header)
    res = requests.post(url=url,data=request_body)
    print(res.json())
    return res


if __name__ == "__main__":
    path = "/v1/task/status"
    ip = "http://hwa-grayapp.avlyun.com"
    method = "POST"
    tpl = "hw-a"
    secret_key = "2v8cmc6tjisxmyy8tt6pt6mttbvrtzsk"
    header = {"Content-Type": "application/json"}
    request_body = '{    "request":[        {           "task_id":"6a7bad7c-09c3-47c0-ad14-38d3efd2e038",      	  "type": ["compliance"]        }    ]}'
    encryption(ip=ip, path=path, method=method, tpl=tpl, secret_key=secret_key,request_body=request_body)
