from jsonpath import jsonpath
import requests
# from common.request_handler import Http
from common import request_handler
from common.yaml_handler import myconf


class List():
    '''
    def __init__(self,url,method,param=None,cookie=None):
        super(List,self).__init__(url,method,param=None,cookie=None)
        self.list=self.http()
    def list(self):
        return self.list
     '''

    @staticmethod
    def id():
        res = request_handler.Http(myconf.get('list', 'url'), myconf.get('list', 'method')).http()
        return jsonpath(res.json(), "$..id")[0]


if __name__ == '__main__':
    import sys
