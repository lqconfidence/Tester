"""
 -----*--------------*-------
__author__ :  yangyali
__time__ : '2020/5/28'
-*- coding: utf-8 -*-
 -----*--------------*-------
"""
from threading import Thread

import requests


class MyThread(Thread):  #
    def run(self):
        get_result(id)


def get_result(id):
    res = requests.get('id')
    '''结果写回表格'''


for i in range(100):
    id = requests.get('获取id')
    '''id存进表格'''
    '''开启一个线程'''
    t1=MyThread()
    t1.start()
    '''循环读取表格得到一个列表嵌套字典'''
    '''遍历列表，判断每个字典的结果列是否为空并且flag是否为1，不为且不为1时进行解析'''
    '''解析'''
    '''在表格写一列flag,解析完的flag为1'''
