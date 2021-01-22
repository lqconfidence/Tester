# -*-coding:utf-8 -*-
# @Time:2020/8/17 16:11
# @Author:a'nan
# @Email:934257271
# @File:wf_login.py
import requests
import jsonpath

class LoginToken():
    def login_token(self):
        url = "http://psp.avlyun.org/api/auth/v1/login"

        request_body = {"username":"ouyangrui1","password":"om/257271"}
        res = requests.post(url=url, json=request_body)
        print("login的token为{}".format(res.json()))
        token = jsonpath.jsonpath(res.json(), "$..token")[0]
        return token

    def auth_token(self,login_token):
        url = 'http://workflow-admin.test.k8ss.cc/v1/graph'
        request_body = {"query":"query auth($token:String!)"
                                "{\n  authentication(token:$token)"
                                "{\n    expire\n    id\n    name\n    token\n    }\n}",
                        "variables":{"token":"{}".format(login_token)},"operationName":"auth"}
        res = requests.post(url=url, json=request_body)
        print(res)
        print("authtoken为{}".format(res.json()))
        auth_token = jsonpath.jsonpath(res.json(), "$..token")[0]
        return auth_token


if __name__ == '__main__':
    login_token = LoginToken().login_token()
    auth_token = LoginToken().auth_token(login_token)
    print(auth_token)