from configparser import ConfigParser
from common.setting import Config


class MyConfig(ConfigParser):

    def __init__(self):
        super().__init__()
        self.read(Config.config_path, encoding='utf_8')

    isinstance = None
    count = 0

    def __new__(cls, *args, **kwargs):
        if not cls.isinstance:
            cls.isinstance = super().__new__(cls)
            cls.count += 1
            return cls.isinstance
        else:
            return cls.isinstance

    def __str__(self):
        return 'config object'


myconf = MyConfig()
res=myconf.get('loger','name')
#print(res)
