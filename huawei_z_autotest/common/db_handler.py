import pymysql
#import yaml
from pymysql.cursors import DictCursor

from common.setting import Config
from common.yaml_handler import MyConfig

class DBHandler:
    # __slots__ = ['conn', 'cursor']

    # def __new__(cls, *args, **kwargs):
    #     return super.__new__(cls)

    def __init__(self):
        myconf = MyConfig()
        self.con = pymysql.connect(host=myconf.get('database', 'host'),
                                   port=eval(myconf.get('database', 'port')),
                                   user=myconf.get('database', 'user'),
                                   password=myconf.get('database', 'password'),
                                   charset='utf8')
        self.cur = self.con.cursor()

    def query(self, sql, args=None, one=True):
        try:
            self.cur.execute(sql, args)
            self.con.commit()
            if one:
                return self.cur.fetchone()
            else:
                return self.cursor.fetchall()
        except Exception as e:
            raise e

    # 获取查询到的第一条数据
    def get_one(self, sql):
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    # 获取查询到的记录条数
    def get_count(self, sql):
        self.con.commit()
        return self.cur.execute(sql)

    # 获取查询到的所有数据
    def get_all(self, sql):
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    # 获取查询到的多条数据
    def get_many(self, sql, size=3):
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchmany(size)

    # 关闭连接
    def close(self):
        # 关闭有标对象
        self.cur.close()
        # 关闭连接对象
        self.con.close()

        # finally:
        #     self.cursor.close()

if __name__ == "__main__":
    db = DBHandler()
    sql="select result from `public_api_test`.tasks where task_id = '75290213-0e9f-479e-b6ec-96b49b762bbb'"
    res = db.get_one(sql=sql)[0]
    print("更新至public-api的结果是{}，类型为{}".format(res, type(res)))

# db_connect = DBHandler(Config.db_host, Config.db_port, Config.db_user, Config.db_password, Config.db_charset,
#                        Config.db_database).query("select * from devices;")

#cursor = DBHandler(Config.db_host, Config.db_port, Config.db_user, Config.db_password, Config.db_charset,                   Config.db_database)
# if __name__ == "__main__":
# coursor = DBHandler(Config.db_host, Config.db_port, Config.db_user, Config.db_password, Config.db_charset,
#                     Config.db_database)
# result = coursor.query("select device_group,device_id from devices;")
#
# print("device_id: %s" % result[1])
# db = pymysql.connect(Config.db_host, Config.db_user, Config.db_password,
#                      Config.db_database)
# fw = db.cursor()
# fw.execute("select * from devices;")
#
# data = fw.fetchone()
# print(data)
