import json
import requests
from scripts.handle_log import do_logger

class HandleRequest:
    def __init__(self):
        self.one_re = requests.Session()

    def to_request(self, url, method='post', data=None, is_json=False, header=None):
        method = method.lower()
        if method == "get":
            res = self.one_re.get(url, params=data, headers=header)
        elif method == "post":
            if is_json:
                res = self.one_re.post(url, json=data, headers=header)
            else:
                res = self.one_re.post(url, data=data, headers=header)
        else:
            res = None
            do_logger.error("不支持【{}】方法请求".format(method))
        return res

    def close(self):
        self.one_re.close()

if __name__ == '__main__':
    re_url = "http://mykong.avlyun.com:9124/open/fusion/v2/sql/query"
    re_params = {"sql":"select * from tidb_hw_dev_score_0308_last where keyhash16='cbc426079d795806'"}
    headers = {'x-access-key':'eCOYRgDPnaLFiK52','Content-Type':'application/json'}
    one_request = HandleRequest()
    rep = one_request.to_request(method='post', url=re_url, data=re_params, is_json=True, header=headers)
    print(rep.text)
    actual_result = rep.text.encode('utf-8').decode("unicode_escape")
    print(actual_result)
    final_result = json.loads(actual_result)
    print(final_result)
    print(type(re_params))