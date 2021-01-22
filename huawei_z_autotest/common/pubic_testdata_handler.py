""""
*************
Author:ouyangrui
Time:2020/4/26
Email:934257271@qq.com
********************
"""
from common.db_handler import DBHandler


# 目前主要用于外网模块的task_id和MD5的替换
class HandlerPublicTestData():
    db = DBHandler()

    # 将原始参数替换为从数据库查出来的第一条md5
    def handler_md5(self, data, sql):
        replace_md5 = str(self.db.get_one(sql)[0])
        # print(replace_id,type(replace_id))
        return data.replace('#md5#', replace_md5)

    # 替换一个task_id
    def handler_task_id(self, data, sql):
        replace_task_id = str(self.db.get_one(sql)[0])
        # print(replace_id, type(replace_id))
        return data.replace('#task_id#',replace_task_id)


    #替换指定字符串
    def handler_test_data(self, data, sql, before_str):
        replace_data = self.db.get_one(sql)[0]
        return data.replace(before_str, replace_data)


if __name__ == '__main__':
    data = '{    "request":[       {        "task_id":"#task_id#11",     "md5":"#md5#",   "type": ["compliance"]    }  ]}'
    hdt = HandlerPublicTestData()
    sql = 'select task_id from `public-api`.tasks ORDER BY created_at ASC'
    sql1 = 'select md5 from `public-api`.tasks ORDER BY created_at ASC'
    betaskid = '#task_id#'
    bemd5 = '#md5#'

    res1 = hdt.handler_test_data(data=hdt.handler_test_data(data=data, sql=sql, before_str=betaskid),sql=sql1, before_str=bemd5)
    print(res1)
