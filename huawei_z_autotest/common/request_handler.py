import requests

from common.loger_handler import mylog


class Http():
    def __init__(self, url, method, json=None, param=None, cookie=None):
        self.url = url
        self.method = method
        self.param = param
        self.cookie = cookie
        self.json = json

    def http(self):
        res = None
        if self.method.upper() == 'GET':
            try:
                res = requests.get(self.url, params=self.param, cookies=self.cookie)
            except Exception as e:
                mylog.error('request _get error the reason is {}'.format(e))
        elif self.method.upper() == 'POST':
            try:
                # example 有问题，这里的json一直都是空，因为没有传值过来
                res = requests.post(self.url, data=self.param, json=self.json, cookies=self.cookie)
            except Exception as e:
                mylog.error('request _get error the reason is {}'.format(e))
        else:
            mylog.error('request method error')
            res = res
        return res


#     可以返回res = res.json()等各种格式


if __name__ == '__main__':
    a = []
    if a:
        print("空值为真")
    else:
        print("空值为假")
