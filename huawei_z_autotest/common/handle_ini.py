#！/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__  = admin

import os
import sys
import configparser

base_path=os.path.dirname(os.getcwd())
sys.path.append(base_path)

class Myparse(configparser.ConfigParser):
    def parse_dict(self):
        d=dict(self._sections)
        for k in d:
            d[k]=dict(d[k])
        return d


class HandInit:

    def __init__(self,file_name):
        self.file_path=base_path+"/common/" + file_name #CheckingRateConfig.ini

    def load_user_ini(self):
        # file_path=base_path+"/common/CheckingRateConfig.ini"
        cf=configparser.ConfigParser()
        cf.read(self.file_path,encoding="utf-8-sig")
        return cf

    def load_manger_ini(self):
        file_path=base_path+"/Config/server_admin.ini"
        cf=configparser.ConfigParser()
        cf.read(file_path,encoding="utf-8-sig")
        return cf

    def get_userIni_value(self,key,node = 'server'):
        cf=self.load_user_ini()
        try:
            data = cf.get(node, key)
        except Exception:
            data = None
        return data

    def get_managerIni_value(self,key,node = "server"):
        cf = self.load_manger_ini()
        try:
            data = cf .get(node,key)
        except Exception:
            data = None
        return data


if __name__== "__main__":
    h=HandInit("CheckingRateConfig.ini")
    myparse=Myparse()
    myparse.read(h.file_path,encoding="utf-8")
    print(myparse.parse_dict())
